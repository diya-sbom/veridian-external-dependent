Project: Veridian

Problem:
AI agents can execute actions without an independent verification layer.

What Veridian does:
Veridian introduces verification before execution and state validation after execution.

Current Proofs:
- External dependency proof
- ALLOW → EXECUTION_ALLOWED
- DENY → HALT
- Ledger-backed verification records

Question:
Would a verification gate that can halt agent execution before action be useful in your workflow?

GitHub:


Core:
https://github.com/diya-sbom/mira

Dependency Example:
https://github.com/diya-sbom/veridian-external-dependent
