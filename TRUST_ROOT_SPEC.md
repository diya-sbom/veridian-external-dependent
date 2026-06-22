# Veridian Trust Root Specification

## Purpose

The Trust Root establishes who is allowed to act within Veridian.

Without trusted identity:

- actions cannot be attributed
- receipts cannot be trusted
- accountability cannot be proven

## Goal

Bind:

Agent
Action
State
Receipt

to a verifiable identity.

---

## Trust Root Responsibilities

1. Agent Identity
2. Agent Authentication
3. Agent Authorization
4. Receipt Signing
5. Key Lifecycle

---

## Verification Rule

No verified identity:

FAIL CLOSED

No execution.

---

## Evidence Rule

Every receipt must contain:

agent_id
timestamp
receipt_hash
signature

---

## Accountability Rule

Veridian must be able to prove:

Who acted
What was done
What changed
What evidence exists
