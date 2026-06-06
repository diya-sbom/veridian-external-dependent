Subject:
Independent verification for AI agents

Message:

We are building Veridian, a verification layer for AI agents.

Veridian verifies actions before execution and validates resulting state after execution.

Current proofs include:

- External dependency enforcement
- ALLOW → EXECUTION_ALLOWED
- DENY → HALT
- Verification receipts
- Ledger-backed continuity

Question:

Would a verification gate that can halt agent execution before action be useful in your workflow?

Repositories:

https://github.com/diya-sbom/mira
https://github.com/diya-sbom/veridian-external-dependent
