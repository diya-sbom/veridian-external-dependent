# Deterministic Replay Specification

## Purpose

Deterministic Replay allows Veridian to reconstruct and verify a historical execution.

A verifier must be able to replay the execution using recorded evidence and reach the same verified outcome.

## Replay Inputs

- Agent Identity
- Action Receipt
- State Receipt
- Execution Timestamp
- Policy Version
- Verification Rules Version

## Replay Rule

Replay must reproduce:

- verified action
- verified state
- receipt chain
- evidence chain

## Failure Rule

Missing receipt:
FAIL CLOSED

Missing evidence:
FAIL CLOSED

State mismatch:
FAIL CLOSED

## Guarantee

Given the same inputs,
the same verification outcome must be produced.
