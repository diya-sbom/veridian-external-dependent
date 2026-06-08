import json
import hashlib
from pathlib import Path

LEDGER = Path("bil/bil_ledger.jsonl")

def canonical_hash(record):
    data = json.dumps(record, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()

def verify_continuity():
    if not LEDGER.exists():
        print("BIL_CONTINUITY_FAIL: ledger missing")
        return False

    previous_hash = "GENESIS"

    with open(LEDGER) as f:
        for line_number, line in enumerate(f, start=1):
            entry = json.loads(line)

            if entry.get("previous_record_hash") != previous_hash:
                print(f"BIL_CONTINUITY_FAIL: line {line_number}")
                return False

            record_hash = entry.get("record_hash")
            if not record_hash:
                print(f"BIL_CONTINUITY_FAIL: missing record_hash line {line_number}")
                return False

            previous_hash = record_hash

    print("BIL_CONTINUITY_PASS")
    return True

if __name__ == "__main__":
    verify_continuity()
