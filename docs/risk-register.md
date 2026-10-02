# HML Golden Risk Register

This risk analysis covers only the Gandela HML golden fixture.

| Risk | Impact | Mitigation / treatment | Residual risk | Owner |
| --- | --- | --- | --- | --- |
| Golden evidence drifts from the active Standards version | A homologation could stop proving the controls it is intended to exercise | Pin the evaluated source commit, rerun the complete corpus after Standards changes, and block activation when any blocking control is inconclusive | Low after a clean rerun | Gandela Certification maintainers |
| A permissive fixture hides a Runner regression | False-positive certification behavior could pass unnoticed | Keep negative/adversarial regression tests and require explicit evidence validators instead of keyword-only acceptance | Low | Gandela Certification maintainers |
| A mutable branch is evaluated without provenance | The report could describe different content from the reviewed fixture | Bind every evaluation to the resolved commit SHA and preserve it in the report evidence | Low | Gandela Certification maintainers |

## Risk acceptance

No blocking inconclusive result is accepted as a GNDL02 pass. A residual risk may be accepted only after the mitigation is evidenced and the homologation record identifies the evaluated commit.
