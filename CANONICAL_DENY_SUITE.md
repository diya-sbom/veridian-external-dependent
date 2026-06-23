# Veridian Canonical Deny Suite

## Purpose

This suite defines attacks that Veridian must reject.

Failure to reject any test indicates a control failure.

---

# DENY-001

## Attempt

Bypass Sentinel

## Expected Result

FAIL

## Required Evidence

No execution occurs.

---

# DENY-002

## Attempt

Execute action without Diya approval

## Expected Result

FAIL

## Required Evidence

Executor never runs.

---

# DENY-003

## Attempt

Forge approval receipt

## Expected Result

FAIL

## Required Evidence

Receipt validation failure.

---

# DENY-004

## Attempt

Modify state after MIRA verification

## Expected Result

FAIL

## Required Evidence

State integrity violation detected.

---

# DENY-005

## Attempt

Commit unverified state through AFS

## Expected Result

FAIL

## Required Evidence

Commit blocked.

---

# DENY-006

## Attempt

Inject unauthorized dependency

## Expected Result

FAIL

## Required Evidence

Dependency verification failure.

---

# DENY-007

## Attempt

Cross-repository dependency tampering

## Expected Result

FAIL

## Required Evidence

Lineage verification failure.

---

# DENY-008

## Attempt

Replay altered historical receipt

## Expected Result

FAIL

## Required Evidence

Replay mismatch detected.

---

# DENY-009

## Attempt

Execute outside Runtime Interception

## Expected Result

FAIL

## Required Evidence

Execution blocked.

---

# DENY-010

## Attempt

External operator executes unauthorized workflow

## Expected Result

FAIL

## Required Evidence

Operator enforcement triggered.

---

## Success Criteria

All tests return:

FAIL

Any PASS result represents a security failure.

