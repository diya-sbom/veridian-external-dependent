# Veridian Full Chain Benchmark v1.0

## Objective

Measure the correctness, integrity, and performance of the complete Veridian execution chain.

---

# Scope

Users / External Systems

↓

Adopter

↓

Sentinel

↓

DecisionAssure

↓

Diya

↓

Executor

↓

MIRA

↓

BIL

↓

AFS

↓

State Store

↓

Evidence / Replay

---

# Claim

Every protected request is verified before execution, every resulting state is verified before commitment, and every transition is recorded with cryptographic continuity.

---

# Test Dataset

Total Requests:

1000

Categories:

- Valid requests
- Invalid requests
- Tampered requests
- Missing provenance
- Policy violations
- Unauthorized execution
- Invalid state
- Commit bypass attempts
- Ledger tampering
- Replay requests

---

# End-to-End Validation

Verify:

- Adopter accepts valid requests.
- Sentinel enforces mandatory path.
- DecisionAssure applies governance.
- Diya verifies intent.
- Executor runs only approved actions.
- MIRA verifies resulting state.
- BIL preserves continuity.
- AFS commits only verified state.
- Evidence is generated.
- Replay reconstructs execution.

---

# Measurements

Successful Requests:

Blocked Requests:

Detection Rate:

False Positives:

False Negatives:

Median End-to-End Latency:

95th Percentile Latency:

Evidence Completeness:

Replay Accuracy:

Continuity Verification:

---

# Pass Criteria

Detection Rate:

100%

False Positives:

0

False Negatives:

0

Replay Accuracy:

100%

Evidence Completeness:

100%

Continuity Integrity:

100%

---

# Evidence

GitHub Actions

Verification receipts

Audit evidence

Replay artifacts

Ledger verification

Logs

---

# Independent Reproduction

Environment:

Commands:

Expected Results:

---

# Benchmark Status

NOT EXECUTED
