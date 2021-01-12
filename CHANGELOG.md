## 📜 Changelog

This documents the changes from release to release.


### 0.0.8

-   Addresses https://github.com/MCLConsortium/mcl.sickbay/issues/2 by:
    -   Adding `inscribed_participant_ID` and `inscribed_specimen_ID` to `Genomics`
    -   Adding `inscribed_participant_ID` and `inscribed_specimen_ID` to `Imaging`
    -   Adding `inscribed_participant_ID` to `Biospecimen`
    -   (It also adds some test data to these fields.)


### 0.0.7

In this release:

-   The `labcasFileURL` field is now just `labcasID`; everything else is the same except the name (and the semantics; it no longer is used to hold URLs)
-   The `Organ` class now has an `inscribed_participant_ID` field you can use to note a future participant ID association with a `ClinicalCore`
-   All enumerations now use [advanced enumerations](https://pypi.org/project/aenum/) for their base class.
-   All enumerations now have a case-insensitive lookup.

The implications of that last bullet mean:

```python
>>> from mcl.sickbay.model.enums import Race
>>> Race.black_or_african_american == Race('Black or African American')
True
>>> Race.black_or_african_american == Race['Black or African American']
True
>>> Race.black_or_african_american == Race['black or african american']
True
>>> Race('black or african american')
Traceback (most recent call last):
...
ValueError: 'black or african american' is not a valid Race
```

So if you want case-insensitive lookups, use brackets, not parentheses.


### 0.0.6

In this release:

-   Base metadata for all classes now includes:
    -   `consortium`, a nullable string that can be used to contain an RDF URI to the consortium that originated the data, such as `https://mcl.nci.nih.gov/` for the Consortium for Molecular and Cellular Characterization of Screen-Detected Lesions.
    -   `protocolID`, a nullable integer that tells the research protocol that generated the data.
-   Kristen's sample data (`--add-sample-data`) includes these consortium and protocol IDs


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
