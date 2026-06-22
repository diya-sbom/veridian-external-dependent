# Trust Root Proof

## Objective

Prove that every Veridian receipt can be traced to a verified identity.

## Proof Chain

Verified Identity
        ↓
Authorized Agent
        ↓
Verified Action
        ↓
Verified State
        ↓
Signed Receipt
        ↓
Evidence

## Failure Rule

Missing Identity:
FAIL CLOSED

Unauthorized Identity:
FAIL CLOSED

Invalid Signature:
FAIL CLOSED

## Veridian Guarantee

Veridian must be able to prove:

Who acted
What action was taken
What state changed
What receipt was generated
What evidence exists
