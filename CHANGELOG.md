## 📜 Changelog

This documents the changes from release to release.


### 1.1.0

This release contains some incompatible changes in order to accommodate CDE updates from 2021-08-26 through 2021-11-18. Please [see the CDE changelog](https://mcl.nci.nih.gov/resources/standards/mcl_cdedictionaries_changelog-4.xlsx) for highly pedantic details of these updates. The changes to the software include:

-   On class `Organ`:
    -   `histopathology_precancer_type` was a 1-to-many attribute of `LungOrgan` only; now it belongs to _all_ organs as 1-to-many.
    -   This base class now has the following optional attributes:
        -   `ajcc_clinical_m`
        -   `ajcc_clinical_n`
        -   `ajcc_clinical_t`
        -   `ajcc_clinical_stage`
        -   `ajcc_pathologic_m`
        -   `ajcc_pathologic_n`
        -   `ajcc_pathologic_t`
        -   `ajcc_pathologic_stage`
        -   `lymph_nodes_tested`
        -   `lymph_node_location`
-   On the class `LungOrgan`:
    -   There are _numerous_ changes. For one, the `ajcc_staging_system_edition` indicates whether the entire record uses the AJCC Staging edition 7 or 8, and depending on this, it tells which set of attributes to use.
        -   The attributes are:
            -   `ajcc_7_lung_clinical_m`
            -   `ajcc_7_lung_clinical_n`
            -   `ajcc_7_lung_clinical_t`
            -   `ajcc_7_lung_disease_stage`
            -   `ajcc_7_lung_pathologic_m`
            -   `ajcc_7_lung_pathologic_n`
            -   `ajcc_7_lung_pathologic_t`
            -   `ajcc_8_lung_clinical_m`
            -   `ajcc_8_lung_clinical_n`
            -   `ajcc_8_lung_clinical_t`
            -   `ajcc_8_lung_disease_stage`
            -   `ajcc_8_lung_pathologic_m`
            -   `ajcc_8_lung_pathologic_n`
            -   `ajcc_8_lung_pathologic_t`
        -   Note that all of these attributes are _optional_; this is because it's also possible that `ajcc_staging_system_edition` is `unknown` or `not_reported`, in which case we can't enforce that a specific set of the above attributes are actually used.
    -   Lungs also have a new attribute: `lymph_nodes_positive`, an optional integer.
-   On the class `ProstateOrgan`, these attributes have moved "up" into the superclass `Organ`:
    -   `lymph_nodes_tested`
    -   `lymph_node_location`
    -   `ajcc_clinical_m`
    -   `ajcc_clinical_n`
    -   `ajcc_clinical_t`
    -   `ajcc_clinical_stage`
    -   `ajcc_pathologic_m`
    -   `ajcc_pathologic_n`
    -   `ajcc_pathologic_t`
    -   `ajcc_pathologic_stage`
-   In class `Biospecimen`, these attributes were required and are now optional:
        -   `days_to_collection`
        -   `time_excision_to_processing`
        -   `days_to_storage`
-   The following enumerated types have changed:
    -   `TStage7` no longer includes the terms `t1c` or `t1mi`
    -   `ClinicalMStage7` has dropped the terms `M1c` and `pM1`
    -   For `GroupStage7`, the following permissible values are no longer permissible:
        -   `ia1`
        -   `ia2`
        -   `ia3`
        -   `iva`
        -   `ivb`
    -   `Precancers` now includes a `normal` kind
    -   `Fixatives` now supports a `not_applicable` value
    -   When it comes to `Storage` you now have two new options
        -   `room_temperature_then_refrigerated`
        -   `frozen_at__20c`
    -   `SlideCharges` has made these values impermissible: `cm0`, `cm1`, `pm1`, `pm1a`, `pm1b`, `pm1c`
    -   We now finally have a blessed description for `Treatment` instead of the kind contrived by a mere software developer
    -   At long last an expert has realized that `cannot_be_determine` should be `cannot_be_determined` in `Necrosis`
    -   The following new enumerations are ready for use:
        -   `ClinicalMStage8` with 8 values
        -   `ClinicalNStage8` with 7 values
        -   `GroupStage8` with 17 values
        -   `AJCCMetastasisStage8` with 8 values
-   Removal of [zc.buildout](http://www.buildout.org/en/latest/). We cannot recommend this tool less. Just use virtual environments like everyone else.


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
