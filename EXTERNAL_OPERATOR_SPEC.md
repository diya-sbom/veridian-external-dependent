# External Operator Specification

## Purpose

External Operators are entities that perform actions outside the direct control of Veridian.

Examples:

- Human operators
- Vendors
- SaaS providers
- Cloud providers
- External APIs
- Third-party agents

## Requirement

External actions must be attributable.

Veridian must record:

- operator identity
- action performed
- timestamp
- evidence
- resulting state

## Verification Rule

Unknown operator:
FAIL CLOSED

Missing evidence:
FAIL CLOSED

Missing attribution:
FAIL CLOSED

## Accountability Rule

Every external action must be linked to a verifiable operator.

## Guarantee

Veridian can identify:

Who acted

What action occurred

What evidence exists

What state changed
