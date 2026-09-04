"""H4087: synthesize the decisions.json for the H3346 Type-D concordance
store-merge vote. MG's ruling (vote h3346_typed_store, mega-sheet card 25,
04-09-2026) was a bulk policy approval -- "Type-D concordance merges into
CommentaryStrategies store" -- not a per-card vote on the 258-row review
sheet. This script is the paper trail for treating that bulk ruling as the
vote-equivalent: every row is marked approve, none rejected.
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "data" / "typed_link_sundara_concordance.jsonl"
OUT = (REPO / "data" / "analysis" / "typed_link_sundara" /
       "commentarystrategies-sundarakanda-typed-link-q41_decisions.json")

rows = [json.loads(line) for line in SRC.read_text(encoding="utf-8").splitlines()]
reviewer_decisions = {
    r["_row_key"]: {"action": "approve"} for r in rows
}

payload = {
    "sheet_id": "commentarystrategies-sundarakanda-typed-link-q41",
    "source": "Uprava vote h3346_typed_store (mega-sheet uprava-drain-assumptions_04-09-26, "
              "card 25) -- MG ruling 'approve (a)', 04-09-2026: bulk merge of the whole "
              "258-row Type-D concordance, not a per-card review-sheet vote.",
    "reviewer_decisions": reviewer_decisions,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True),
                encoding="utf-8")
print(f"wrote {len(reviewer_decisions)} approve decisions -> {OUT}")
