## 📜 Changelog

This documents the changes from release to release.


### 0.0.5

This release fixes:

-   In `BreastOrgan`, the field `her2_in_situ_hybridization` was the wrong enumerated type. It should've been `HER2InSituHybridization`.
-   In the enums, add the type `HER2InSituHybridization`.
-   Add test data from `12_78_BreastCore_20200625_0`.
-   Removed foreign key constraint from `Biospecimen.specimen_parent_ID` because the parent ID may be either another biospecimen or could be a participant (clinical core) object.
-   New class `AdjacentSpecimen` to work around circular dependency problem of having adjacent specimens directly on `Biospeciment`.
-   New JSON serialization for `adjacent_specimens` on `Biospecimen`
-   Misspelled enumeration `AnatomicalSite`: `pancrease` → `pancreas`
-   Change `create-demo-db` to `create-clinical-db` since this is no longer a demo but the real deal
-   Transition from old style `setup.py` to everything in `setup.cfg`

In this release, 0.0.5, we also finally start keeping a changelog 😮
