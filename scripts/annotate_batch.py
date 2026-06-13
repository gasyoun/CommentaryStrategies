"""
Year 1 annotation pipeline — batch note classification via Anthropic API.

Input:  sources/{translator}_notes.json
        Array of objects with at minimum: {"raw_text": "..."}
        Optional fields carried through: comment_id, shloka_addr, editor

Output: data/{translator}_full.json
        Array of fully classified annotation records per commentary_schema.json

Usage:
    python scripts/annotate_batch.py sementsov
    python scripts/annotate_batch.py sementsov --limit 50 --model claude-sonnet-4-6
    python scripts/annotate_batch.py sementsov --dry-run

Resumable: skips notes already in the output file (matched by comment_id).
"""

import sys, json, re, time, argparse, pathlib

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

ROOT   = pathlib.Path(__file__).parent.parent
PROMPTS = ROOT / "prompts"
SOURCES = ROOT / "sources"
DATA    = ROOT / "data"

DEFAULT_MODEL = "claude-haiku-4-5-20251001"   # cheapest; upgrade to sonnet for quality check

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


# ── Classification ─────────────────────────────────────────────────────────────

def classify_note(client, system_prompt: str, raw_text: str, translator: str,
                  model: str) -> dict:
    """Call Anthropic API. Returns parsed classification dict."""
    import anthropic

    message = client.messages.create(
        model=model,
        max_tokens=512,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"Translator: {translator}\n\nNote:\n{raw_text}"
        }]
    )
    text = message.content[0].text.strip()

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

def run(translator: str, model: str, limit: int | None, dry_run: bool) -> None:
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
        print(f"[DRY RUN] Would classify {total - len(done_indices)} notes using {model}")
        for i, note in enumerate(notes[:3]):
            print(f"  [{i+1}] {note['raw_text'][:80]}...")
        return

    system_prompt = load_system_prompt()

    try:
        import anthropic
    except ImportError:
        print("ERROR: anthropic package not installed. Run: pip install anthropic")
        sys.exit(1)

    client = anthropic.Anthropic()

    # Preflight: verify credentials AND model resolve BEFORE the loop. Without
    # this, a missing key errors through every note (the 401 is swallowed as a
    # per-note "error") and an empty output file gets written — looking like a
    # run that "did nothing". One cheap, token-free call fails fast instead.
    no_creds_msg = ("ERROR: no valid Anthropic credentials. Set ANTHROPIC_API_KEY "
                    "(or ANTHROPIC_AUTH_TOKEN, or run `ant auth login`) and retry.")
    try:
        client.models.retrieve(model)
    except anthropic.AuthenticationError:
        # Key present but rejected by the server (401).
        print(no_creds_msg)
        sys.exit(2)
    except anthropic.PermissionDeniedError:
        print(f"ERROR: these credentials lack permission for model {model!r}.")
        sys.exit(2)
    except anthropic.NotFoundError:
        print(f"ERROR: unknown model {model!r}. Check --model.")
        sys.exit(2)
    except anthropic.APIError as e:
        # Transient/other (rate limit, overload, network): warn but proceed —
        # the main loop has its own per-note handling.
        print(f"WARNING: preflight inconclusive ({type(e).__name__}: {e}); proceeding.")
    except Exception as e:
        # No credential configured at all: the SDK raises TypeError ("Could not
        # resolve authentication method") locally, before any request is sent.
        print(no_creds_msg)
        print(f"  ({type(e).__name__}: {e})")
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
            classification = classify_note(client, system_prompt, raw, translator, model)
            record = normalise(raw, classification, i, translator)
            # Carry through optional fields from source
            for field in ("shloka_addr", "editor"):
                if field in note:
                    record[field] = note[field]
            results.append(record)
            print(f"✓ {record['axis_2_kazansky']} {record['axis_4_paribok']}"
                  f"{' FF:' + ','.join(record['false_friends']) if record['false_friends'] else ''}")
        except (anthropic.AuthenticationError, anthropic.PermissionDeniedError) as e:
            # Fatal config error — every remaining call fails identically. Abort
            # now (break, not exit) so the guarded save below preserves whatever
            # already succeeded; the run is resumable.
            print(f"\nFATAL: {type(e).__name__}: {e}")
            print("Aborting — fix credentials/permissions, then re-run (resumable).")
            break
        except Exception as e:
            errors += 1
            print(f"ERROR: {e}")

        # Incremental save every 20 notes (only if we have something to save)
        if results and i % 20 == 0:
            output_file.write_text(
                json.dumps(results, ensure_ascii=False, indent=2),
                encoding="utf-8", newline="\n")

        # Rate limit: ~6 req/s max for Haiku, stay well below
        time.sleep(0.2)

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
        description="Batch annotate translator notes via Anthropic API")
    parser.add_argument("translator",
        help="Translator slug (e.g. sementsov, burba, petrov)")
    parser.add_argument("--limit", type=int, default=None,
        help="Process only first N notes (for testing)")
    parser.add_argument("--model", default=DEFAULT_MODEL,
        help=f"Anthropic model ID (default: {DEFAULT_MODEL})")
    parser.add_argument("--dry-run", action="store_true",
        help="Print what would be done without calling the API")
    args = parser.parse_args()

    run(args.translator, args.model, args.limit, args.dry_run)
