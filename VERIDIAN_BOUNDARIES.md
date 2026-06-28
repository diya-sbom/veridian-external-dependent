# Veridian Boundaries

## Purpose

This document defines the scope of Veridian.

It describes the responsibilities that belong to Veridian and those intentionally delegated to external systems.

---

# Veridian Responsibilities

Veridian is responsible for:

* Execution integrity
* Action verification
* State verification
* Fail-closed enforcement
* Runtime enforcement
* Tamper-evident evidence
* Signed receipts
* Deterministic replay
* Continuity and lineage
* Trust verification
* Multi-repository dependency integrity
* Governance evidence

---

# Out of Scope

Veridian is not responsible for:

* Identity management
* User authentication
* Workforce identity lifecycle
* Access management
* Secret management
* Certificate authority services
* General-purpose policy authoring
* Operating system security
* Network security
* Vulnerability scanning
* Endpoint protection
* SIEM functionality

These capabilities are expected to be provided by external systems where appropriate.

---

# External Integrations

Veridian is designed to integrate with:

* Identity providers
* Authentication systems
* Policy engines
* CI/CD platforms
* Build systems
* Source code repositories
* Runtime environments
* Audit platforms
* Evidence repositories

---

# Design Philosophy

Veridian does not replace existing security platforms.

Instead, it provides an execution-integrity layer that connects trusted identity, verified execution, validated state transitions, and auditable evidence.

---

# Architectural Boundary

Identity answers:

"Who is acting?"

Authorization answers:

"What is permitted?"

Veridian answers:

"What actually happened?"

"What changed?"

"Can it be independently verified?"

---

# Mission

Enable organizations to move from trust-based autonomous systems to evidence-based autonomous systems through verifiable execution integrity.

