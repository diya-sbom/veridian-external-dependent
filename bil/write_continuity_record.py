import json
import hashlib
import time
from pathlib import Path

LEDGER = Path("bil/bil_ledger.jsonl")

def canonical_hash(record):
    data = json.dumps(record, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()

def last_record_hash():
    if not LEDGER.exists():
        return "GENESIS"

    lines = LEDGER.read_text().strip().splitlines()
    if not lines:
        return "GENESIS"

    last_entry = json.loads(lines[-1])
    return last_entry["record_hash"]

def append_record(event_type, decision):
    previous_hash = last_record_hash()

    record = {
        "event_type": event_type,
        "decision": decision,
        "timestamp": int(time.time()),
        "previous_record_hash": previous_hash,
    }

    record["record_hash"] = canonical_hash(record)

    LEDGER.parent.mkdir(exist_ok=True)
    with open(LEDGER, "a") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")

    print("BIL_RECORD_WRITTEN")
    print(record["record_hash"])

if __name__ == "__main__":
    append_record("TEST_CONTINUITY_RECORD", "ALLOW")
