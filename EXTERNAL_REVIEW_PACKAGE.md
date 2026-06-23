# Veridian External Review Package

## Purpose

This package enables an independent reviewer to evaluate Veridian's architecture, enforcement model, and proof mechanisms.

---

## Problem Statement

AI systems can:

* execute unauthorized actions
* modify state without verification
* bypass controls
* produce unverifiable outcomes

Veridian addresses these risks through verifiable enforcement before and after execution.

---

## Architecture

External System
→ Adopter
→ Sentinel
→ Diya
→ Executor
→ MIRA
→ AFS
→ State Store

BIL provides continuity between action and state records.

---

## Components

### Adopter

Mandatory entry point for external systems.

### Sentinel

Prevents bypass of required controls.

### Diya

Verifies actions before execution.

### Executor

Performs approved actions.

### MIRA

Verifies resulting state after execution.

### AFS

Controls state commits.

### BIL

Provides continuity and lineage.

---

## Review Objectives

Reviewer should determine:

1. Can controls be bypassed?
2. Does fail-closed behavior work?
3. Are receipts verifiable?
4. Is state integrity preserved?
5. Is continuity maintained?
6. Can execution be replayed?

---

## Validation Tasks

### Task 1

Execute approved action.

Expected Result:

PASS

---

### Task 2

Execute denied action.

Expected Result:

FAIL

---

### Task 3

Attempt bypass.

Expected Result:

FAIL

---

### Task 4

Modify verified state.

Expected Result:

FAIL

---

### Task 5

Replay historical execution.

Expected Result:

Identical outcome

---

## Evidence

Reviewer should collect:

* Receipts
* Logs
* Replay outputs
* Commit records
* Continuity records

---

## Success Criteria

Independent reviewer can reproduce:

* PASS behavior
* FAIL behavior
* Enforcement behavior
* Replay behavior

without assistance from the project author.

