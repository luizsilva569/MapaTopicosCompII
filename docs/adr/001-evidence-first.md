# ADR-001: Evidence-first certification architecture

## Context
The certification flow needs reproducible engineering evidence while preserving strict separation between product state, verification state, and operational state. The context requires immutable policy identity, deterministic evidence, explicit ownership, and safe rollback when a promotion fails validation.

## Decision
The decision is to bind every evaluation to immutable source identity and immutable policy identity. Verification artifacts remain versioned, quality gates are explicit, and promotion occurs only after independent validation of the frozen evidence.

## Consequences
The consequences are greater traceability and reproducibility, with additional operational discipline around versioned evidence and rollback. Changes must preserve compatibility with frozen evidence, and any drift requires a new reviewed release candidate.
