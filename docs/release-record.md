# HML Golden Release Record

This document describes only the versioned Gandela HML golden fixture. It is not a production deployment record.

## Current release

Release **v1.4.29-golden.1** is published on the `gandela-hml-gndl02-golden` branch as the reference corpus for Standards 1.4.29.

The release contains the frozen evidence set used to validate GNDL01 and GNDL02 controls in homologation.

## Rollback procedure

Rollback is performed by restoring the golden branch to the last approved golden commit and rerunning the homologation against that immutable commit.

A rollback is accepted only when the candidate report is regenerated and its source commit is recorded in the homologation evidence.
