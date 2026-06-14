# Trust Roots Protocol

Version: 1.0

Status: Draft

## Purpose

Trust roots define who is allowed to issue, sign, verify, approve, or revoke Veridian receipts.

Signed receipts are not enough unless the signer is trusted.

## Core Rule

A receipt is trusted only if:

- the receipt is valid
- the signature is valid
- the issuer belongs to a trusted root
- the trust root has not been revoked

## Trusted Issuer Record

Required fields:

- issuer_id
- public_key_id
- role
- granted_by
- timestamp
- signature

## Revocation Record

Required fields:

- issuer_id
- revoked_by
- timestamp
- reason
- signature

## Roles

- Owner
- Administrator
- Verifier
- Reviewer
- Operator

## Failure Rule

If issuer trust cannot be verified, the receipt must fail closed.

## Invariant

No trusted issuer
→ no trusted receipt.
