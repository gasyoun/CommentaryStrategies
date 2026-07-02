"""
Year 1 annotation pipeline — batch note classification via a pluggable LLM backend.

Backends (choose with --backend or $LLM_BACKEND; default: openai):
  • openai    — any OpenAI-compatible Chat Completions endpoint (OpenAI, OpenRouter,
                Gemini's OpenAI-compat API, YandexGPT, local Ollama/vLLM/LM Studio …).
                Config via env:
                  LLM_API_KEY   (or OPENAI_API_KEY)  — required
                  LLM_BASE_URL  — optional; omit for api.openai.com, set for others
                  LLM_MODEL     — optional default model id (or pass --model)
  • anthropic — Anthropic Messages API (needs ANTHROPIC_API_KEY).

Input:  sources/{translator}_notes.json
        Array of objects with at minimum: {"raw_text": "..."}
        Optional fields carried through: comment_id, shloka_addr, editor

Output: data/{translator}_full.json
        Array of fully classified annotation records per commentary_schema.json

Usage:
    # OpenAI-compatible (default backend)
    export LLM_API_KEY=...                # your provider key
    export LLM_MODEL=gpt-4o-mini          # provider-specific; --model overrides
    python scripts/annotate_batch.py kalyanov --limit 5
    python scripts/annotate_batch.py kalyanov --limit 50

    # OpenRouter / Gemini / YandexGPT / local — same backend, different base_url:
    export LLM_BASE_URL=https://openrouter.ai/api/v1
    export LLM_MODEL=google/gemini-2.0-flash-001

    # Anthropic (only if you have a key):
    python scripts/annotate_batch.py kalyanov --backend anthropic

    # Offline smoke test (no API call, no key needed):
    python scripts/annotate_batch.py kalyanov --dry-run

See docs/ANNOTATION_BACKENDS.md for per-provider recipes.
Resumable: skips notes already in the output file (matched by comment_id).
"""

import sys, os, json, re, time, argparse, pathlib

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT   = pathlib.Path(__file__).parent.parent
PROMPTS = ROOT / "prompts"
SOURCES = ROOT / "sources"
DATA    = ROOT / "data"

# Per-backend default model — used only when neither --model nor $LLM_MODEL is set.
DEFAULT_MODELS = {
    "openai":    "gpt-4o-mini",                 # cheap, capable; override per provider
    "anthropic": "claude-haiku-4-5-20251001",   # cheapest; upgrade to sonnet for quality
}

IAST_RE = re.compile(r'[āĀīĪūŪṛṚṭṬḍḌṇṆśŚṣṢṃṀḥḤñṅḷ]')

VALID_TOPICS   = {"sanskrit_term","myth","context","realia","geography","reference","textology","philosophy"}
VALID_KAZANSKY = {"A","B","V","G"}
VALID_PARIBOK  = {"P","K","D"}
VALID_LAKSHANA = {"L1","L2","L3","L4","L5"}


# ── Prompt loading ─────────────────────────────────────────────────────────────

def load_system_prompt() -> str:
    path = PROMPTS / "classify_note.md"
    if not path.exists():
        raise FileNotFoundError(f"Classification prompt not found: {path}")
    return path.read_text(encoding="utf-8")


# ── LLM backends ─────────────────────────────────────────────────────────────────
#
# A backend wraps one provider SDK and exposes three methods:
#   complete(system_prompt, user_content, model) -> raw reply text
#   preflight(model) -> None if creds+model+endpoint resolve, else an error string
#   is_fatal(exc)    -> True if a mid-loop exception is a config error (abort, not skip)
# Everything provider-specific lives here; the rest of the pipeline is backend-agnostic.

class AnthropicBackend:
    """Anthropic Messages API. Needs ANTHROPIC_API_KEY (or ANTHROPIC_AUTH_TOKEN)."""
    name = "anthropic"

    def __init__(self):
        try:
            import anthropic
        except ImportError:
            print("ERROR: anthropic package not installed. Run: pip install anthropic")
            sys.exit(1)
        self._sdk = anthropic
        self.client = anthropic.Anthropic()

    def complete(self, system_prompt: str, user_content: str, model: str) -> str:
        message = self.client.messages.create(
            model=model,
            max_tokens=512,
            system=system_prompt,
            messages=[{"role": "user", "content": user_content}],
        )
        return message.content[0].text.strip()

    def preflight(self, model: str) -> str | None:
        a = self._sdk
        no_creds = ("no valid Anthropic credentials. Set ANTHROPIC_API_KEY "
                    "(or ANTHROPIC_AUTH_TOKEN), then retry.")
        try:
            self.client.models.retrieve(model)        # cheap, token-free
            return None
        except a.AuthenticationError:
            return no_creds
        except a.PermissionDeniedError:
            return f"credentials lack permission for model {model!r}."
        except a.NotFoundError:
            return f"unknown model {model!r}. Check --model / $LLM_MODEL."
        except a.APIError as e:
            print(f"WARNING: preflight inconclusive ({type(e).__name__}: {e}); proceeding.")
            return None
        except Exception as e:
            return f"{no_creds}\n  ({type(e).__name__}: {e})"

    def is_fatal(self, exc: Exception) -> bool:
        return isinstance(exc, (self._sdk.AuthenticationError, self._sdk.PermissionDeniedError))


class OpenAIBackend:
    """Any OpenAI-compatible Chat Completions endpoint, selected by env:
        LLM_API_KEY / OPENAI_API_KEY  — key (required)
        LLM_BASE_URL                  — endpoint (optional; default = api.openai.com)
    Covers OpenAI, OpenRouter, Gemini (OpenAI-compat), YandexGPT, local servers.
    """
    name = "openai"

    def __init__(self):
        try:
            import openai
        except ImportError:
            print("ERROR: openai package not installed. Run: pip install openai")
            sys.exit(1)
        self._sdk = openai
        api_key = os.environ.get("LLM_API_KEY") or os.environ.get("OPENAI_API_KEY")
        base_url = os.environ.get("LLM_BASE_URL") or None
        if not api_key:
            print("ERROR: no API key. Set LLM_API_KEY (or OPENAI_API_KEY); for "
                  "non-OpenAI providers also set LLM_BASE_URL. "
                  "See docs/ANNOTATION_BACKENDS.md.")
            sys.exit(2)
        self.base_url = base_url or "https://api.openai.com/v1"
        self.client = (openai.OpenAI(api_key=api_key, base_url=base_url)
                       if base_url else openai.OpenAI(api_key=api_key))

    def complete(self, system_prompt: str, user_content: str, model: str) -> str:
        resp = self.client.chat.completions.create(
            model=model,
            max_tokens=512,
            temperature=0,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
        )
        return (resp.choices[0].message.content or "").strip()

    def preflight(self, model: str) -> str | None:
        o = self._sdk
        try:
            # Minimal end-to-end probe: validates key + endpoint + model in one cheap call.
            self.client.chat.completions.create(
                model=model, max_tokens=1,
                messages=[{"role": "user", "content": "ping"}],
            )
            return None
        except o.AuthenticationError:
            return (f"API key rejected (401) at {self.base_url}. "
                    "Check LLM_API_KEY / OPENAI_API_KEY.")
        except o.PermissionDeniedError:
            return f"permission denied (403) at {self.base_url}."
        except o.NotFoundError:
            return (f"model {model!r} not found at {self.base_url}. "
                    "Set --model / $LLM_MODEL.")
        except o.BadRequestError as e:
            return f"bad request for model {model!r}: {e}. Check --model / $LLM_MODEL."
        except o.APIError as e:
            print(f"WARNING: preflight inconclusive ({type(e).__name__}: {e}); proceeding.")
            return None
        except Exception as e:
            print(f"WARNING: preflight could not run ({type(e).__name__}: {e}); proceeding.")
            return None

    def is_fatal(self, exc: Exception) -> bool:
        return isinstance(exc, (self._sdk.AuthenticationError, self._sdk.PermissionDeniedError))


def make_backend(name: str):
    if name == "anthropic":
        return AnthropicBackend()
    if name == "openai":
        return OpenAIBackend()
    print(f"ERROR: unknown backend {name!r}. Use --backend openai|anthropic.")
    sys.exit(1)


# ── Classification ───────────────────────────────────────────────────────────────

def classify_note(backend, system_prompt: str, raw_text: str, translator: str,
                  model: str) -> dict:
    """Send one note to the active backend; parse the JSON object from its reply."""
    user_content = f"Translator: {translator}\n\nNote:\n{raw_text}"
    text = backend.complete(system_prompt, user_content, model)

    # Extract JSON block (model may wrap in ```json ... ```)
    m = re.search(r'\{.*\}', text, re.DOTALL)
    if not m:
        raise ValueError(f"No JSON found in model response: {text[:200]}")
    return json.loads(m.group())


# ── Validation & normalisation ─────────────────────────────────────────────────

def normalise(raw: str, classification: dict, note_index: int,
              translator: str) -> dict:
    """Merge raw input fields with classification output; validate; fill defaults."""
    topics   = [t for t in classification.get("axis_1_topic", []) if t in VALID_TOPICS]
    kazansky = classification.get("axis_2_kazansky", "G")
    if kazansky not in VALID_KAZANSKY:
        kazansky = "G"
    lakshana = [l for l in classification.get("axis_3_lakshana", []) if l in VALID_LAKSHANA]
    paribok  = classification.get("axis_4_paribok", "P")
    if paribok not in VALID_PARIBOK:
        paribok = "P"

    # has_iast: trust regex, use LLM as fallback if regex gives False
    has_iast_regex = bool(IAST_RE.search(raw))
    has_iast = has_iast_regex or classification.get("has_iast", False)

    return {
        "comment_id":               f"{translator}/comment_{note_index:04d}",
        "translator":               translator,
        "raw_text":                 raw,
        "char_count":               len(raw),
        "has_iast":                 has_iast,
        "axis_1_topic":             topics if topics else ["context"],
        "axis_2_kazansky":          kazansky,
        "axis_3_lakshana":          lakshana,
        "axis_4_paribok":           paribok,
        "false_friends":            classification.get("false_friends", []),
        "cited_indian_commentators": classification.get("cited_indian_commentators", []),
        "cited_western_sources":    classification.get("cited_western_sources", []),
    }


# ── Pipeline ───────────────────────────────────────────────────────────────────

def run(translator: str, backend_name: str, model: str, limit: int | None,
        dry_run: bool, sleep: float) -> None:
    source_file = SOURCES / f"{translator}_notes.json"
    output_file = DATA    / f"{translator}_full.json"

    if not source_file.exists():
        print(f"ERROR: source file not found: {source_file}")
        print(f"  Expected format: array of objects with 'raw_text' field.")
        print(f"  See sources/README.md for format specification.")
        sys.exit(1)

    notes: list[dict] = json.loads(source_file.read_text(encoding="utf-8"))
    if limit:
        notes = notes[:limit]
    total = len(notes)
    print(f"Loaded {total} notes from {source_file.name}")

    # Load existing results for resumability
    results: list[dict] = []
    if output_file.exists():
        results = json.loads(output_file.read_text(encoding="utf-8"))
        print(f"Resuming: {len(results)} notes already classified")
    done_indices = {r["comment_id"] for r in results}

    if dry_run:
        print(f"[DRY RUN] backend={backend_name} model={model} — would classify "
              f"{total - len(done_indices)} notes (no API call).")
        for i, note in enumerate(notes[:3]):
            print(f"  [{i+1}] {note['raw_text'][:80]}...")
        return

    system_prompt = load_system_prompt()
    backend = make_backend(backend_name)
    print(f"Backend: {backend_name}   model: {model}")

    # Preflight: verify credentials AND model resolve BEFORE the loop. Without this,
    # a missing key / bad model errors through every note (looking like a run that
    # "did nothing", with an empty output file). One cheap call fails fast instead.
    err = backend.preflight(model)
    if err:
        print(f"ERROR: {err}")
        sys.exit(2)

    errors = 0

    for i, note in enumerate(notes, start=1):
        cid = f"{translator}/comment_{i:04d}"
        if cid in done_indices:
            continue

        raw = note.get("raw_text", "").strip()
        if not raw:
            print(f"  [{i}/{total}] SKIP (empty raw_text)")
            continue

        print(f"  [{i}/{total}] {cid} ({len(raw)} chars)...", end=" ", flush=True)

        try:
            classification = classify_note(backend, system_prompt, raw, translator, model)
            record = normalise(raw, classification, i, translator)
            # Carry through optional fields from source
            for field in ("shloka_addr", "editor"):
                if field in note:
                    record[field] = note[field]
            results.append(record)
            print(f"✓ {record['axis_2_kazansky']} {record['axis_4_paribok']}"
                  f"{' FF:' + ','.join(record['false_friends']) if record['false_friends'] else ''}")
        except Exception as e:
            # Fatal config error (bad key/permission) — every remaining call fails
            # identically. Abort now (break, not exit) so the guarded save below
            # preserves whatever already succeeded; the run is resumable.
            if backend.is_fatal(e):
                print(f"\nFATAL: {type(e).__name__}: {e}")
                print("Aborting — fix credentials/permissions, then re-run (resumable).")
                break
            errors += 1
            print(f"ERROR: {e}")

        # Incremental save every 20 notes (only if we have something to save)
        if results and i % 20 == 0:
            output_file.write_text(
                json.dumps(results, ensure_ascii=False, indent=2),
                encoding="utf-8", newline="\n")

        # Gentle throttle; raise --sleep for low-RPM free tiers (e.g. Gemini free).
        time.sleep(sleep)

    # Never write an empty output file — it would create misleading resume state
    # and look like real output.
    if results:
        output_file.write_text(
            json.dumps(results, ensure_ascii=False, indent=2),
            encoding="utf-8", newline="\n")
        print(f"\nComplete: {len(results)} notes classified, {errors} errors → {output_file}")
    else:
        print(f"\nNo notes classified ({errors} errors); output file not written.")
    if errors:
        print(f"  Re-run to retry failed notes (pipeline is resumable).")


# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Batch-annotate translator notes via a pluggable LLM backend "
                    "(OpenAI-compatible by default; Anthropic optional).")
    parser.add_argument("translator",
        help="Translator slug (e.g. kalyanov, sementsov, burba)")
    parser.add_argument("--backend", choices=["openai", "anthropic"], default=None,
        help="LLM backend (default: $LLM_BACKEND or 'openai').")
    parser.add_argument("--model", default=None,
        help="Model id. Precedence: --model > $LLM_MODEL > per-backend default "
             "(openai: gpt-4o-mini, anthropic: claude-haiku-4-5-20251001).")
    parser.add_argument("--limit", type=int, default=None,
        help="Process only the first N notes (for testing).")
    parser.add_argument("--sleep", type=float, default=0.2,
        help="Delay between calls, seconds (raise for low-RPM free tiers). Default 0.2.")
    parser.add_argument("--dry-run", action="store_true",
        help="Print what would be done without calling any API (no key needed).")
    args = parser.parse_args()

    backend_name = args.backend or os.environ.get("LLM_BACKEND", "openai")
    model = args.model or os.environ.get("LLM_MODEL") or DEFAULT_MODELS.get(backend_name)
    if not model:
        print(f"ERROR: no model for backend {backend_name!r}. Pass --model or set $LLM_MODEL.")
        sys.exit(1)

    run(args.translator, backend_name, model, args.limit, args.dry_run, args.sleep)
