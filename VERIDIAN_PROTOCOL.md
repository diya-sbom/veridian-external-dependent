# Veridian Protocol Specification

Version: 1.0

Status: Draft

---

## Purpose

Veridian provides independent verification of agent actions, state transitions, and commit operations.

The protocol answers:

* What action was requested?
* Was the action permitted?
* Was it executed?
* Did the resulting state match the claim?
* Is there proof?
* Can verification be bypassed?

---

# Protocol Flow

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

# Record Types

## Intent Record

Generated before execution.

Purpose:

Verify requested action.

Required Fields:

* record_type
* timestamp
* action
* decision
* verifier
* record_hash

Valid Decisions:

* ALLOW
* DENY

Failure Rule:

DENY MUST prevent execution.

---

## State Record

Generated after execution.

Purpose:

Verify resulting state.

Required Fields:

* record_type
* timestamp
* expected_state
* observed_state
* decision
* verifier
* record_hash

Valid Decisions:

* PASS
* FAIL

Failure Rule:

FAIL MUST prevent commit.

---

## Commit Record

Generated before state persistence.

Purpose:

Authorize commit.

Required Fields:

* record_type
* timestamp
* commit_decision
* verifier
* record_hash

Valid Decisions:

* COMMIT
* REJECT

Failure Rule:

REJECT MUST prevent state persistence.

---

# Receipt Rules

Every verification decision SHALL generate a receipt.

Minimum Fields:

* timestamp
* decision
* verifier
* record_hash

Receipts SHALL be immutable.

---

# Continuity Rules

All BIL records SHALL contain:

* record_hash
* previous_record_hash

Genesis Record:

previous_record_hash = GENESIS

Continuity Failure:

Verification history SHALL be considered invalid if continuity verification fails.

---

# Sentinel Rule

Verification steps SHALL NOT be bypassable.

Any attempt to bypass verification SHALL fail closed.

---

# AFS Rule

State SHALL NOT be committed without successful verification.

---

# Protocol Guarantee

Veridian does not guarantee correctness of an action.

Veridian guarantees that actions, state transitions, and commit decisions are independently verified, recorded, and auditable.

