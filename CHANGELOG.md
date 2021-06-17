## 📜 Changelog

This documents the changes from release to release.


### 1.0.2

For issue https://github.com/EDRN/MCL-metadata/issues/22

-   Additional permissible value on `sequencing_platform` (enum `GenomicAnalyzer`), namely `illumina_hiseq_1500`.
-   Changed the `read_length` from numeric to a string (10)
-   Note that we do not have schema migrations set up so these steps must be run manually:
    -   `ALTER TABLE "genomics" ALTER "read_length" SET DATA TYPE CHARACTER VARYING(10)`
    -   `ALTER TYPE "genomic_analyzier_enum" ADD VALUE 'illumina_hiseq_1500' AFTER 'illumina_genome_analyzer_iix'`


### 1.0.1

- This version adds the human-readable label plus the token value to all enumerations over the JSON; see https://github.com/MCLConsortium/mcl.sickbay/issues/16 for more information.


### 1.0.0

- A "more official" release.


### 0.0.10


For issue https://github.com/MCLConsortium/mcl.sickbay/issues/1:

-   On `ClinicalCore`:
    -   The `race` attribute is now a 1-to-many mapping to `CoreRace` via `core_races`
    -   The `type_tobacco_used` is now a 1-to-many mapping to `CoreTobacco` via `core_tobaccos`
    -   The attribute `days_to_birth` is now required
-   On `Biospecimen`:
    -   The enumeration for `Precancers` has a whole bunch of new permitted values
-   On `BreastOrgan`:
    -   The enumeration for `PrecancerousHistopathology` contains values for "unknown" and "data not available"
    -   The enumeration for `BreastSite` now has an `unknown` value
    -   A new value `pending` is available for `GeneticTestingAnswer`, `TestResults`, `EstrogenTestResults`
    -   The enumeration `HER2Results` adds `pending` and `unknown` values
    -   The enumeration `BreastImagingWorkup` adds an `unknown` value
    -   The enumeration `BIRADSTissues` adds values for "unknown" and "data not available"
-   New `LungOrgan` plus (bogus) test data for it
-   New `PancreasOrgan` plus (bogus) test data for it
-   Updated `ProstateOrgan`
    -   Previously, this was just a placeholder to test multiple inheritance from the common `Organ` class in terms of both Python class hierachy and database hierarchy
    -   Now it's completely filled out with the `v0` prostate common data elements with its numerous controlled vocabularies
-   Expanded enumerations: `ClinicalMStage7`, `TStage7`, `ClinicalNStage7`, `GroupStage7`, `MarginalStatus`
-   New enumerations, far too many to enumerate 😏

For issue https://github.com/MCLConsortium/mcl.sickbay/issues/4:

-   All fields in `LabCASMetadata` are now `String`.

For issue https://github.com/MCLConsortium/mcl.sickbay/issues/3:

-   `inscribed_clinicalCore_participant_ID` is a new field on `PriorLesion`, `CoreRace`, and `CoreTobacco`
-   `inscribed_biospecimen_identifier` is a new field on `AdjacentSpecimen`

For issue https://github.com/MCLConsortium/mcl.sickbay/issues/5:

-   The following updates diverge from the [data dictionaries](https://mcl.nci.nih.gov/resources/standards/mcl-cdes) of the common data elements:
    -   `participant_ID` is now 50 characters (along with foreign keys and `inscribed` fields), up from 14
    -   `specimen_ID` is now 50 characters (along with foreign keys and `inscribed` fields), up from 16

And finally, for issue https://github.com/MCLConsortium/mcl.sickbay/issues/6 … we add `unknown` to all enumerations that didn't have it already.



### 0.0.9

-   Rename `inscribed_participant_ID` → `inscribed_clinicalCore_participant_ID`
-   Rename `inscribed_specimen_ID` → `inscribed_biospecimen_specimen_ID`


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
