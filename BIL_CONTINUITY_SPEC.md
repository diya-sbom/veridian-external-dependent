# BIL Continuity Specification

Purpose

Provide cryptographic continuity between verification events.

Rule

Each ledger entry SHALL contain:

- record_hash
- previous_record_hash
- timestamp
- decision

Genesis Entry

The first entry SHALL use:

previous_record_hash = "GENESIS"

Continuity Rule

Entry N MUST contain the record_hash
of Entry N-1.

Failure Rule

If continuity is broken:

- verification fails
- ledger integrity is invalid
- audit proof is rejected

Goal

Prove that verification history
cannot be silently altered,
reordered, or truncated.
