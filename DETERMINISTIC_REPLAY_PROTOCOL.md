# Deterministic Replay Protocol

Version: 1.0

Status: Draft

## Purpose

Deterministic replay enables independent reconstruction of a Veridian decision path.

The goal is to answer:

- What happened?
- Why did it happen?
- Can it be reproduced?

## Replay Record

Required Fields:

- request_id
- timestamp
- input_hash
- policy_hash
- verifier_version
- decision
- receipt_hash

## Replay Rule

Given identical:

- inputs
- policies
- verifier version

the replay process SHALL produce the same decision.

## Failure Rule

If replay cannot reproduce the original decision, the record SHALL be considered non-reproducible.

## Audit Rule

Replay records SHALL be retained as evidence.

## Invariant

Same inputs
+
Same policy
+
Same verifier

→ Same decision
