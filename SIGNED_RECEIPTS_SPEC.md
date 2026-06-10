# Signed Receipts Specification

Version: 1.0

Status: Draft

## Purpose

Signed receipts bind a Veridian verification decision to a trusted issuer.

Hashing proves integrity.

Signing proves origin.

## Current Receipt Fields

- timestamp
- decision
- verifier
- record_hash

## Signed Receipt Fields

A signed receipt SHALL include:

- timestamp
- decision
- verifier
- record_hash
- issuer
- signature
- signature_algorithm

## Signing Rule

The signature SHALL be created over the canonical receipt payload excluding the `signature` field.

## Verification Rule

A signed receipt is valid only if:

1. required fields exist
2. record_hash matches the canonical payload
3. issuer is trusted
4. signature verifies
5. signature_algorithm is supported

## Failure Rule

If signature verification fails, the receipt SHALL be rejected.

## Trust Rule

Unsigned receipts MAY be used for local testing.

Signed receipts are REQUIRED for external trust and enterprise use.

## Invariant

No valid signature
→ no trusted external receipt.
