# Access Control Protocol

Version: 1.0

Status: Draft

---

## Purpose

Veridian verifies actions, state transitions, and commit operations.

This protocol defines who may access Veridian, what actions they may perform, and how access changes are recorded.

The goal is:

* Controlled access
* Auditable permissions
* Signed authorization
* Verifiable revocation
* Non-bypassable governance

---

# Roles

## Viewer

Permissions:

* Read documentation
* Read receipts
* Read evidence

Restrictions:

* No execution authority
* No policy modification
* No administrative actions

---

## Reviewer

Permissions:

* Review receipts
* Review verification decisions
* Review continuity records

Restrictions:

* Cannot execute actions
* Cannot modify policies
* Cannot grant access

---

## Operator

Permissions:

* Execute approved workflows
* Submit verification requests

Restrictions:

* Cannot modify protocol
* Cannot manage trust roots
* Cannot grant access

---

## Administrator

Permissions:

* Manage policies
* Manage operational configuration
* Approve access requests

Restrictions:

* Cannot modify protocol guarantees

---

## Owner

Permissions:

* Modify protocol specifications
* Manage trust roots
* Approve protocol changes
* Approve administrative access

---

# Access Grant Record

Every access grant SHALL generate a receipt.

Required Fields:

* user
* role
* granted_by
* timestamp
* reason
* signature

---

# Access Revocation Record

Every access revocation SHALL generate a receipt.

Required Fields:

* user
* role
* revoked_by
* timestamp
* reason
* signature

---

# Trust Rule

No access change SHALL be considered valid without an associated signed record.

---

# Audit Rule

All access grants and revocations SHALL be retained as immutable evidence.

---

# Governance Rule

Permissions SHALL be explicitly granted.

Permissions SHALL NOT be implicitly inherited.

---

# Protocol Guarantee

Veridian treats access changes as governed events.

Access, approval, modification, and revocation SHALL be independently recorded and auditable.

