# Veridian Demo

## Purpose

This demo shows how Veridian controls autonomous agent execution.

The goal is simple:

- Verify action before execution
- Verify state after execution
- Generate receipts
- Preserve ledger continuity
- Fail closed when verification fails

---

## Architecture

External System
↓
Adopter
↓
Sentinel
↓
Diya
↓
BIL
↓
Executor
↓
MIRA
↓
BIL
↓
AFS
↓
BIL
↓
State Store

---

## Scenario 1: ALLOW Path

Agent requests an action.

Veridian verifies:

- action is valid
- execution is allowed
- receipt is generated
- BIL continuity is preserved

Expected result:

```text
EXECUTION_ALLOWED


Receipt:

{
  "decision": "ALLOW",
  "record_hash": "..."
}


Scenario 2: DENY Path

Agent requests an action that is not permitted.

Veridian returns:

DENY

Expected result:

HALT: decision denied

Execution does not proceed.

State is not committed.


Scenario 3: Continuity Proof

BIL records are chained using:

previous_record_hash


Expected result:

BIL_CONTINUITY_PASS


If a record is deleted, inserted, modified, or reordered:

BIL_CONTINUITY_FAIL



Scenario 4: Signed Receipt Proof

Receipts can be signed and verified.

Expected result:

SIGNATURE_VALID


If a receipt is modified after signing:

SIGNATURE_INVALID

