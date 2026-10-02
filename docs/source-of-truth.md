# Source of Truth and Ownership

This document applies only to the Gandela HML golden fixture.

## Canonical source

The **source of truth** for the golden fixture is the versioned content of the `gandela-hml-gndl02-golden` branch in `luizsilva569/MapaTopicosCompII`.

The branch commit is the **canonical source** for source code, tests, quality configuration, release evidence, and engineering documentation used by a homologation run.

## State owner

**State owner / ownership:** the Gandela Certification maintainers are responsible for the golden fixture state.

The certification Portal owns the policy snapshot used by a run. The Runner owns the immutable execution evidence it produces. Neither component may silently replace the branch commit used as the authoritative source for the evaluated fixture.
