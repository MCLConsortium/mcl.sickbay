# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Database related interations.
'''


from . import VERSION
from .model import createMetadata
from .model.clinicalcore import ClinicalCore, PriorLesion
from .model.specimens import Biospecimen, AdjacentSpecimen
from .model.genomics import Genomics, Smart3SeqGenomics
from .model.images import Imaging
from .model.organs import Organ, BreastOrgan, ProstateOrgan, HistopathologyPrecancerType
from .model.enums import (
    Anchors, Gender, Ethnicity, Race, Specimen, AnatomicalSite, Education, Income, PolarAnswer,
    Lesion, Detection, Mode, Neoplasm, ImpertinentAnswer, SmokingStatus, ImpertinentPolarAnswer,
    Tobacco, PrecancerousHistopathology, Grade, Laterality, BreastSite, MysteriousPolarAnswer, NecrosisLocation,
    GeneticTestingAnswer, TestResults, EstrogenTestResults, HER2Results, Menopause, ECOGScore,
    BreastCancerDetectionMethod, BreastImagingWorkup, BIRADSTissues, SequencingTechnique, SequencingOrigin,
    GenomicMethod, GenomicStranding, GenomicAnalyzer, Smart3SeqInput, Smart3SeqIndexing, TumorTissue,
    Precancers, RulesOfAcquisition, Preserves, Fixatives, Analytes, Storage, SlideCharges, VitalStatus,
    MarginalStatus, TStage7, PathologicNStage7, PathologicMStage7, TStage8, PathologicMStage8, ClinicalNStage7,
    ClinicalTNMCategoryN8, HER2InSituHybridization, ClinicalMStage7, GroupStage7, ClinicalTNMCategoryM8,
    PrognosticGroupStage8, Packaging, Destinations
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .json import ClinicalCoreEncoder
import argparse, getpass, datetime, json


_description = '''Generate and populate some database structures for
prototyping purposes. This assumes you've already got a PostgreSQL database
set up and running with permissions to access it.
'''

__version__ = VERSION


def addSampleData(session):
    # Note that 12_111_Biospecimen_20200623_0_DATA contains detached records for some non-existent
    # participant, MCL111_404. Maybe this is a typo and it should be MCL111_400? Or perhaps
    # 12_111_ClinicalCore_20200623_0_DATA had the typo and it should've been MCL111_404?
    # I'm going to assume for now that 12_111_ClinicalCore_20200623_0 contains a typo and it
    # should be MCL111_404 and attach records accordingly.

    # 12_78_ClinicalCore_20200624_0
    cc1 = ClinicalCore(
        # LabCASMetadata
        labcasID='/to/be/determined/1',
        fileName='12_78_ClinicalCore_20200624_0_DATA',
        dateFileGenerated=datetime.date(2020, 2, 13),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=78,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Clinical Core',
        # ClinicalCore
        participant_ID='MCL78_001',
        anchor_type=Anchors.first_positive_biopsy_confirming_diagnosis_date,
        days_to_consent=30,
        days_to_enrollment=30,
        gender=Gender.female,
        ethnicity=Ethnicity.unknown,
        race=Race.native_hawaiian_or_other_pacific_islander,
        vital_status=VitalStatus.alive,
        days_to_vital_status_reference=24,
        age_at_index=49,
        days_to_birth=-17885,
        year_of_birth=1970,
        education=Education.high_school_graduate,
        income=Income.seventy_five_thousand_to_100000,
        height=173,
        days_to_weight_recorded=-450,
        weight=90,
        prior_cancer=PolarAnswer.no,
        current_lesion_type=Lesion.breast,
        days_to_diagnosis=7,
        year_of_diagnosis=2019,
        age_at_diagnosis=49,
        how_detected=Detection.screening,
        days_to_detection_date=0,
        days_to_last_screen_date=-180,
        days_to_last_neg_screen_date=-180,
        mode_of_detection=Mode.imaging,
        lesion_type=Neoplasm.metastatic,
        specimen_collected=PolarAnswer.yes,
        biomarker_tested=PolarAnswer.no,
        relative_with_cancer_history=ImpertinentPolarAnswer.no,
        tobacco_smoking_status=SmokingStatus.never_smoker,
        type_tobacco_used=Tobacco.not_applicable,
        alcohol_history=PolarAnswer.no,
    )
    # 12_78_ClinicalCore_20200624_0
    cc2 = ClinicalCore(
        # LabCASMetadata
        labcasID='/to/be/determined/2',
        fileName='12_78_ClinicalCore_20200624_0_DATA',
        dateFileGenerated=datetime.date(2020, 2, 13),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=78,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Clinical Core',
        # ClinicalCore
        participant_ID='MCL78_003',
        anchor_type=Anchors.first_positive_biopsy_confirming_diagnosis_date,
        days_to_consent=21,
        days_to_enrollment=21,
        gender=Gender.female,
        ethnicity=Ethnicity.hispanic,
        race=Race.white,
        vital_status=VitalStatus.alive,
        days_to_vital_status_reference=10,
        age_at_index=35,
        days_to_birth=-12593,
        year_of_birth=1985,
        education=Education.college_graduate,
        income=Income.greater_than_100000,
        height=147,
        days_to_weight_recorded=0,
        weight=46,
        prior_cancer=PolarAnswer.unknown,
        current_lesion_type=Lesion.breast,
        days_to_diagnosis=8,
        year_of_diagnosis=2020,
        age_at_diagnosis=34,
        how_detected=Detection.symptom_driven_patient_detected,
        days_to_detection_date=-10,
        days_to_last_screen_date=-545,
        days_to_last_neg_screen_date=-545,
        mode_of_detection=Mode.imaging,
        lesion_type=Neoplasm.primary,
        specimen_collected=PolarAnswer.no,
        biomarker_tested=PolarAnswer.yes,
        relative_with_cancer_history=ImpertinentPolarAnswer.yes,
        relative_with_cancer_history_count=3,
        tobacco_smoking_status=SmokingStatus.current_smoker,
        type_tobacco_used=Tobacco.electronic_cigarettes,
        tobacco_smoking_onset_age=16,
        years_smoked=19,
        cigarettes_per_day=8,
        alcohol_history=PolarAnswer.yes,
        alcohol_drinks_per_day=6,
        alcohol_days_per_week=3
    )
    # 12_111_ClinicalCore_20200623_0
    cc3 = ClinicalCore(
        # LabCASMetadata
        labcasID='/to/be/determined/3',
        fileName='12_111_ClinicalCore_20200623_0_DATA',
        dateFileGenerated=datetime.date(2020, 5, 28),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=111,
        submittingInvestigatorID=613,
        processingLevel='Processed',
        fileType='Clinical Core',
        # ClinicalCore
        participant_ID='MCL111_001',
        anchor_type=Anchors.first_imaging_date,
        gender=Gender.male,
        ethnicity=Ethnicity.not_hispanic,
        race=Race.asian,
        vital_status=VitalStatus.dead,
        days_to_vital_status_reference=42,
        age_at_index=68,
        days_to_birth=-24820,
        year_of_birth=1950,
        education=Education.post_high_school_training,
        income=Income.seventy_five_thousand_to_100000,
        height=183,
        days_to_weight_recorded=-100,
        weight=82,
        prior_cancer=PolarAnswer.no,
        current_lesion_type=Lesion.pancreas,
        days_to_diagnosis=20,
        year_of_diagnosis=2018,
        age_at_diagnosis=68,
        how_detected=Detection.screening,
        days_to_detection_date=0,
        days_to_last_screen_date=-368,
        days_to_last_neg_screen_date=-368,
        mode_of_detection=Mode.physical_exam,
        lesion_type=Neoplasm.primary,
        specimen_collected=PolarAnswer.yes,
        biomarker_tested=PolarAnswer.yes,
        relative_with_cancer_history=ImpertinentPolarAnswer.unknown,
        relative_with_cancer_history_count=3,
        tobacco_smoking_status=SmokingStatus.former_smoker,
        type_tobacco_used=Tobacco.pipe,
        tobacco_smoking_onset_age=19,
        tobacco_smoking_quit_age=40,
        years_smoked=21,
        cigarettes_per_day=10,
        alcohol_history=PolarAnswer.yes,
        alcohol_drinks_per_day=1,
        alcohol_days_per_week=1
    )
    # 12_111_ClinicalCore_20200623_0
    cc4 = ClinicalCore(
        # LabCASMetadata
        labcasID='/to/be/determined/3',
        fileName='12_111_ClinicalCore_20200623_0_DATA',
        dateFileGenerated=datetime.date(2020, 5, 28),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=111,
        submittingInvestigatorID=613,
        processingLevel='Processed',
        fileType='Clinical Core',
        # ClinicalCore
        participant_ID='MCL111_404',
        anchor_type=Anchors.first_imaging_date,
        gender=Gender.female,
        ethnicity=Ethnicity.not_hispanic,
        race=Race.asian,
        vital_status=VitalStatus.dead,
        days_to_vital_status_reference=78,
        age_at_index=66,
        days_to_birth=-24024,
        year_of_birth=1953,
        education=Education.some_college,
        income=Income.greater_than_100000,
        height=164,
        days_to_weight_recorded=20,
        weight=74,
        prior_cancer=PolarAnswer.unknown,
        current_lesion_type=Lesion.pancreas,
        days_to_diagnosis=10,
        year_of_diagnosis=2019,
        age_at_diagnosis=65,
        how_detected=Detection.symptom_driven_patient_detected,
        days_to_detection_date=-5,
        days_to_last_screen_date=0,
        days_to_last_neg_screen_date=0,
        mode_of_detection=Mode.physical_exam,
        lesion_type=Neoplasm.primary,
        specimen_collected=PolarAnswer.yes,
        age_at_menses_start=13,
        menses_stop=ImpertinentAnswer.yes,
        age_at_menses_stop=52,
        biomarker_tested=PolarAnswer.yes,
        relative_with_cancer_history=ImpertinentPolarAnswer.unknown,
        relative_with_cancer_history_count=3,
        tobacco_smoking_status=SmokingStatus.not_reported,
        type_tobacco_used=Tobacco.unknown,
        alcohol_history=PolarAnswer.no,
    )
    # 12_78_BreastCore_20200625_0
    o1 = BreastOrgan(
        # LabCASMetadata
        labcasID='/to/be/determined/4',
        fileName='12_78_BreastCore_20200625_0_DATA',
        dateFileGenerated=datetime.date(2020, 6, 24),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=78,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Excel',
        # BreastOrgan
        anchor_type=Anchors.first_positive_biopsy_confirming_diagnosis_date,
        grade=Grade.low,
        laterality=Laterality.left,
        site=BreastSite.upper_outer_quadrant,
        size=4,
        necrosis=MysteriousPolarAnswer.no,
        necrosis_location=NecrosisLocation.data_not_available,
        surgical_margin=MarginalStatus.equivocal,
        recurrence=MysteriousPolarAnswer.no,
        pathologic_T_stage_7=TStage7.tis,
        pathologic_N_stage_7=PathologicNStage7.pn1,
        pathologic_M_stage_7=PathologicMStage7.m1,
        clinical_T_stage_7=TStage7.tis,
        clinical_N_stage_7=ClinicalNStage7.n1,
        clinical_M_stage_7=ClinicalMStage7.m0,
        disease_stage_7=GroupStage7.ia,
        path_TNM_class_T_8=TStage8.tis,
        genetic_testing=GeneticTestingAnswer.done,
        brca1=TestResults.positive,
        brca2=TestResults.unknown,
        estrogen_receptor=EstrogenTestResults.low_positive,
        er_percent_positivity=15,
        progesterone_receptor=TestResults.cannot_be_determined,
        her2_immunohistochemistry=HER2Results.negative_score_0,
        her2_in_situ_hybridization=HER2InSituHybridization.negative_not_amplified,
        ki_67_percent_positive_nuclei=5,
        menopausal_status=Menopause.perimenopausal,
        ecog_score=ECOGScore.s1,
        method_of_detection=BreastCancerDetectionMethod.screening_mammogram,
        days_to_detection_date=-10,
        days_to_last_screening_mammo=-10,
        days_to_last_negative_screening_mammo=-380,
        detected_between_screening_intervals=MysteriousPolarAnswer.no,
        multifocal_disease=MysteriousPolarAnswer.no,
        multicentric_disease=MysteriousPolarAnswer.no,
        imaging_workup=BreastImagingWorkup.mri,
        birads_density=BIRADSTissues.scattered_fibroglandular_densities
    )
    o1.histopathology_precancer_types = [HistopathologyPrecancerType(hp_type=PrecancerousHistopathology.dcis_nos)]
    cc1.organs = [o1]

    bs1 = Biospecimen(
        # LabCASMetadata
        labcasID='/to/be/determined/5/6',
        fileName='12_78_Biospecimen_20200624_0_DATA',
        dateFileGenerated=datetime.date(2020, 2, 13),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=78,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Biospecimen',
        # Biospecimen
        specimen_ID='MCL78_001_10001',
        specimen_ID_local='ABC_123',
        specimen_parent_ID='MCL78_001',
        specimen_type=Specimen.tissue,
        anatomical_site=AnatomicalSite.breast,
        tumor_tissue_type=TumorTissue.primary,
        precancer_type=Precancers.dcis,
        specimen_laterality=Laterality.right,
        acquisition_method=RulesOfAcquisition.incisional_biopsy,
        days_to_collection=0,
        time_excision_to_processing=13,
        ischemic_time=4,
        portion_weight=0.5,
        total_volume=1.5,
        preservation_method=Preserves.cryopreservation_in_liquid_nitrogen_dead_tissue,
        fixative_used=Fixatives.acetone,
        fixation_duration=2,
        processing_duration=17,
        analyte_type=Analytes.dna,
        protocol_number=22,
        protocol_version=1,
        storage_method=Storage.frozen_at__70c,
        days_to_storage=1,
        slide_charge_type=SlideCharges.uncharged,
        section_thickness=15,
        days_to_shipping=2,
        shipping_conditions=Packaging.dry_ice,
        shipping_destination=Destinations.bu
    )
    bs2 = Biospecimen(
        # LabCASMetadata
        labcasID='/to/be/determined/5/7',
        fileName='12_78_Biospecimen_20200624_0_DATA',
        dateFileGenerated=datetime.date(2020, 2, 13),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=78,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Biospecimen',
        # Biospecimen
        specimen_ID='MCL78_001_10002',
        specimen_ID_local='112233_345',
        specimen_parent_ID='MCL78_001',
        specimen_type=Specimen.tissue,
        anatomical_site=AnatomicalSite.breast,
        tumor_tissue_type=TumorTissue.primary,
        precancer_type=Precancers.dcis,
        specimen_laterality=Laterality.right,
        acquisition_method=RulesOfAcquisition.incisional_biopsy,
        days_to_collection=0,
        time_excision_to_processing=13,
        ischemic_time=5,
        portion_weight=0.75,
        total_volume=2,
        preservation_method=Preserves.formalin_fixed_paraffin_embedded_ffpe,
        fixative_used=Fixatives.formalin,
        fixation_duration=3,
        processing_duration=17,
        analyte_type=Analytes.ffpe_dna,
        protocol_number=22,
        protocol_version=1,
        storage_method=Storage.paraffin_block,
        days_to_storage=1,
        slide_charge_type=SlideCharges.unknown,
        section_thickness=21,
        days_to_shipping=2,
        shipping_conditions=Packaging.cold_pack,
        shipping_destination=Destinations.bu
    )
    bs3 = Biospecimen(
        # LabCASMetadata
        labcasID='/to/be/determined/5/8',
        fileName='12_78_Biospecimen_20200624_0_DATA',
        dateFileGenerated=datetime.date(2020, 2, 13),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=78,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Biospecimen',
        # Biospecimen
        specimen_ID='MCL78_001_10003',
        specimen_parent_ID='MCL78_001',
        specimen_type=Specimen.tissue,
        anatomical_site=AnatomicalSite.breast,
        tumor_tissue_type=TumorTissue.primary,
        precancer_type=Precancers.dcis,
        specimen_laterality=Laterality.right,
        acquisition_method=RulesOfAcquisition.incisional_biopsy,
        days_to_collection=0,
        time_excision_to_processing=13,
        ischemic_time=6,
        portion_weight=0.25,
        total_volume=0.75,
        preservation_method=Preserves.formalin_fixed_paraffin_embedded_ffpe,
        fixative_used=Fixatives.formalin,
        fixation_duration=1,
        processing_duration=22,
        analyte_type=Analytes.ffpe_dna,
        protocol_number=22,
        protocol_version=1,
        storage_method=Storage.paraffin_block,
        days_to_storage=1,
        slide_charge_type=SlideCharges.charged,
        section_thickness=3,
        days_to_shipping=2,
        shipping_conditions=Packaging.cold_pack,
        shipping_destination=Destinations.bu
    )
    bs1.adjacent_specimens = [AdjacentSpecimen(adjacent_specimen_ID='MCL78_001_10002')]
    bs2.adjacent_specimens = [AdjacentSpecimen(adjacent_specimen_ID='MCL78_001_10001'), AdjacentSpecimen(adjacent_specimen_ID='MCL78_001_10003')]
    bs3.adjacent_specimens = [AdjacentSpecimen(adjacent_specimen_ID='MCL78_001_10002')]
    cc1.biospecimens = [bs1, bs2, bs3]

    o2 = BreastOrgan(
        # LabCASMetadata
        labcasID='/to/be/determined/4',
        fileName='12_78_BreastCore_20200625_0_DATA',
        dateFileGenerated=datetime.date(2020, 6, 24),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=78,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Excel',
        # BreastOrgan
        anchor_type=Anchors.first_positive_biopsy_confirming_diagnosis_date,
        grade=Grade.intermediate,
        laterality=Laterality.right,
        site=BreastSite.lower_inner_quadrant,
        size=990,
        necrosis=MysteriousPolarAnswer.yes,
        necrosis_location=NecrosisLocation.focal,
        surgical_margin=MarginalStatus.negative_finding,
        recurrence=MysteriousPolarAnswer.yes,
        path_TNM_class_T_8=TStage8.t1mi,
        path_TNM_class_M_8=PathologicMStage8.pm1,
        clinical_TNM_class_T_8=TStage8.t1mi,
        clinical_TNM_class_N_8=ClinicalTNMCategoryN8.cnx,
        clinical_TNM_class_M_8=ClinicalTNMCategoryM8.cm0_i_plus,
        disease_stage_ajcc_8=PrognosticGroupStage8.iia,
        genetic_testing=GeneticTestingAnswer.not_done,
        brca1=TestResults.not_tested,
        brca2=TestResults.not_tested,
        estrogen_receptor=EstrogenTestResults.not_tested,
        progesterone_receptor=TestResults.not_tested,
        her2_immunohistochemistry=HER2Results.not_tested,
        her2_in_situ_hybridization=HER2InSituHybridization.not_tested,
        menopausal_status=Menopause.postmenopausal,
        ecog_score=ECOGScore.s2,
        method_of_detection=BreastCancerDetectionMethod.nipple_discharge,
        days_to_detection_date=-30,
        days_to_last_screening_mammo=-270,
        days_to_last_negative_screening_mammo=-270,
        detected_between_screening_intervals=MysteriousPolarAnswer.yes,
        multifocal_disease=MysteriousPolarAnswer.unknown,
        multicentric_disease=MysteriousPolarAnswer.yes,
        imaging_workup=BreastImagingWorkup.pet_ct,
        birads_density=BIRADSTissues.heterogeneously_dense,
    )
    o2.histopathology_precancer_types = [HistopathologyPrecancerType(hp_type=PrecancerousHistopathology.atypical_ductal_hyperplasia_adh)]
    cc2.organs = [o2]

    bs404_1 = Biospecimen(
        # LabCASMetadata
        labcasID='/to/be/determined/6/1',
        fileName='12_111_Biospecimen_20200623_0_DATA',
        dateFileGenerated=datetime.date(2020, 6, 22),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=111,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Biospecimen',
        # Biospecimen
        specimen_ID='MCL111_404_10001',
        specimen_ID_local='LocalID123',
        specimen_parent_ID='MCL111_404',
        specimen_type=Specimen.tissue,
        anatomical_site=AnatomicalSite.pancreas,
        tumor_tissue_type=TumorTissue.recurrence,
        precancer_type=Precancers.ipmn,
        specimen_laterality=Laterality.not_reported,  # Kristen Anton's test data has this blank, but it's required
        acquisition_method=RulesOfAcquisition.core_biopsy,
        days_to_collection=0,
        time_excision_to_processing=3,
        ischemic_time=2,
        portion_weight=0.67,
        preservation_method=Preserves.formalin_fixed___unbuffered,
        fixative_used=Fixatives.none,
        fixation_duration=11,
        processing_duration=5,
        analyte_type=Analytes.rna,
        protocol_number=1,
        protocol_version=1,
        storage_method=Storage.ambient_temperature,
        days_to_storage=275,
        slide_charge_type=SlideCharges.unknown,
        section_thickness=123,
        days_to_shipping=11,
        shipping_conditions=Packaging.other_shipping,
        shipping_destination=Destinations.ucsf
    )
    bs404_2 = Biospecimen(
        # LabCASMetadata
        labcasID='/to/be/determined/6/2',
        fileName='12_111_Biospecimen_20200623_0_DATA',
        dateFileGenerated=datetime.date(2020, 6, 22),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=111,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Biospecimen',
        # Biospecimen
        specimen_ID='MCL111_404_10002',
        specimen_ID_local='LocalID456',
        specimen_parent_ID='MCL111_404',
        specimen_type=Specimen.tissue,
        anatomical_site=AnatomicalSite.pancreas,
        tumor_tissue_type=TumorTissue.recurrence,
        precancer_type=Precancers.ipmn,
        specimen_laterality=Laterality.not_reported,  # Kristen Anton's test data has this blank, but it's required
        acquisition_method=RulesOfAcquisition.incisional_biopsy,
        days_to_collection=1,
        time_excision_to_processing=4,
        ischemic_time=2,
        portion_weight=0.25,
        preservation_method=Preserves.formalin_fixed___unbuffered,
        fixative_used=Fixatives.none,
        fixation_duration=25,
        processing_duration=7,
        analyte_type=Analytes.repli_g_qiagen_dna,
        protocol_number=1,
        protocol_version=1,
        storage_method=Storage.cut_slide,
        days_to_storage=275,
        slide_charge_type=SlideCharges.not_recorded,
        section_thickness=456,
        days_to_shipping=1,
        shipping_conditions=Packaging.not_recorded,
        shipping_destination=Destinations.ucsf
    )
    bs404_3 = Biospecimen(
        # LabCASMetadata
        labcasID='/to/be/determined/6/3',
        fileName='12_111_Biospecimen_20200623_0_DATA',
        dateFileGenerated=datetime.date(2020, 6, 22),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=111,
        submittingInvestigatorID=1329,
        processingLevel='Processed',
        fileType='Biospecimen',
        # Biospecimen
        specimen_ID='MCL111_404_10003',
        specimen_ID_local='LocalID789',
        specimen_parent_ID='MCL111_404',
        specimen_type=Specimen.tissue,
        anatomical_site=AnatomicalSite.pancreas,
        tumor_tissue_type=TumorTissue.recurrence,
        precancer_type=Precancers.ipmn,
        specimen_laterality=Laterality.not_reported,  # Kristen Anton's test data has this blank, but it's required
        acquisition_method=RulesOfAcquisition.excisional_biopsy,
        days_to_collection=2,
        time_excision_to_processing=5,
        ischemic_time=2,
        portion_weight=1.1,
        preservation_method=Preserves.other,
        preservation_method_other='OtherPreservationMethod',
        fixative_used=Fixatives.other,
        fixatives_other='OtherFixativeType',
        fixation_duration=0,
        processing_duration=22,
        analyte_type=Analytes.other,
        analyte_type_other='OtherAnalyteType',
        protocol_number=1,
        protocol_version=1,
        storage_method=Storage.other,
        storage_method_other='OtherStorageMethod',
        days_to_storage=275,
        slide_charge_type=SlideCharges.not_applicable,
        section_thickness=0.01,
        days_to_shipping=2,
        shipping_conditions=Packaging.ambient_pack,
        shipping_destination=Destinations.ucla
    )
    bs404_1.adjacent_specimens = [AdjacentSpecimen(adjacent_specimen_ID='MCL111_404_10002')]
    bs404_2.adjacent_specimens = [AdjacentSpecimen(adjacent_specimen_ID='MCL111_404_10001'), AdjacentSpecimen(adjacent_specimen_ID='MCL111_404_10003')]
    bs404_3.adjacent_specimens = [AdjacentSpecimen(adjacent_specimen_ID='MCL111_404_10002')]
    cc4.biospecimens = [bs404_1, bs404_2, bs404_3]

    # 12_78_GenomicsSmart3seq_20200624_0_META
    g78_1 = Smart3SeqGenomics(
        labcasID='/to/be/determined/9/1',
        fileName='abcde_VT_3ildhth.fastq',
        dateFileGenerated=datetime.date(2020, 4, 15),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=78,
        submittingInvestigatorID=1327,
        processingLevel='processed',
        fileType='fastq',
        # Genomics
        specimen_ID='MCL78_001_10001',
        sequencing_center=78,
        sequencing_date=datetime.date(2020, 4, 15),
        sequencing_batch_id='ABC123',
        library_name='SSRNASeq5002',
        library_strategy=SequencingTechnique.rna_seq,
        library_source=SequencingOrigin.rna,
        library_selection=GenomicMethod.pcr,
        library_strand=GenomicStranding.first_stranded,
        library_layout=True,
        sequencing_platform=GenomicAnalyzer.illumina_hiseq_2000,
        read_length=250,
        rin=8,
        adapter_name='N702',
        adapter_sequence='TAAGGCGA',
        flow_cell_barcode='ABCD8',
        # Smart3SeqGenomics
        input_type=Smart3SeqInput.tissue_on_cap,
        number_PCR_cycles=3,
        number_libraries_in_pool=2,
        index_sequence='ACGTACGTACGTACGT',
        indexing_type=Smart3SeqIndexing.single,
    )
    bs1.genomics = [g78_1]
    g78_2 = Smart3SeqGenomics(
        labcasID='/to/be/determined/9/2',
        fileName='abcde_VT_3493838.fastq',
        dateFileGenerated=datetime.date(2020, 4, 15),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=78,
        submittingInvestigatorID=1327,
        processingLevel='processed',
        fileType='fastq',
        # Genomics
        specimen_ID='MCL78_001_10002',
        sequencing_center=78,
        sequencing_date=datetime.date(2020, 4, 15),
        sequencing_batch_id='CDE559',
        library_name='SSRNASeq5002',
        library_strategy=SequencingTechnique.rna_seq,
        library_source=SequencingOrigin.rna,
        library_selection=GenomicMethod.affinity_enrichment,
        library_strand=GenomicStranding.second_stranded,
        library_layout=True,
        sequencing_platform=GenomicAnalyzer.illumina_hiseq_2000,  # Kristen Anton has this as "2001" but there's no such permissible value
        read_length=180,
        rin=9,
        adapter_name='A583',
        adapter_sequence='GGACTCCT',
        flow_cell_barcode='ADRG18',
        # Smart3SeqGenomics
        input_type=Smart3SeqInput.tissue_in_tube,
        number_PCR_cycles=6,
        number_libraries_in_pool=5,
        index_sequence='ACGTACGTACGTACGGCATCGT',
        indexing_type=Smart3SeqIndexing.dual,
    )
    bs2.genomics = [g78_2]
    g78_3 = Smart3SeqGenomics(
        labcasID='/to/be/determined/9/3',
        fileName='abcde_VT_32uduus.fastq',
        dateFileGenerated=datetime.date(2020, 4, 15),
        siteID=78,
        submittingInvestigatorID=1327,
        processingLevel='processed',
        fileType='fastq',
        # Genomics
        specimen_ID='MCL78_001_10003',
        sequencing_center=78,
        sequencing_date=datetime.date(2020, 4, 15),
        sequencing_batch_id='154828759',
        library_name='SSRNASeq5002',
        library_strategy=SequencingTechnique.rna_seq,
        library_source=SequencingOrigin.rna,
        library_selection=GenomicMethod.random,
        library_strand=GenomicStranding.unstranded,
        library_layout=False,
        sequencing_platform=GenomicAnalyzer.illumina_hiseq_2000,  # Kristen Anton has this as "2002" but there's no such permissible value
        read_length=60,
        rin=10,
        adapter_name='A447',
        adapter_sequence='CGAGGCTG',
        flow_cell_barcode='KEHS3',
        # Smart3SeqGenomics
        input_type=Smart3SeqInput.rna_in_tube,
        number_PCR_cycles=5,
        number_libraries_in_pool=7,
        index_sequence='ACGTACGTACGTACGTACGGGTTT',
        indexing_type=Smart3SeqIndexing.single,
    )
    bs3.genomics = [g78_3]

    # 12_111_GenomicsSmart3seq_20200625_0_META
    gs111_1 = Smart3SeqGenomics(
        labcasID='/to/be/determined/10/1',
        fileName='RNA334_MDA_3ildhth.fastq',
        dateFileGenerated=datetime.date(2020, 5, 1),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=111,
        submittingInvestigatorID=613,
        processingLevel='raw',
        fileType='fastq',
        # Genomics
        specimen_ID='MCL111_404_10001',
        sequencing_center=111,
        sequencing_date=datetime.date(2020, 5, 1),
        sequencing_batch_id='DIN3333',
        library_name='BkRNASeq_4848',
        library_strategy=SequencingTechnique.rna_seq,
        library_source=SequencingOrigin.bulk_cells,
        library_selection=GenomicMethod.poly_t_enrichment,
        library_strand=GenomicStranding.first_stranded,
        library_layout=True,
        sequencing_platform=GenomicAnalyzer.ion_torrent_pgm,
        read_length=150,
        rin=8,
        adapter_name='H5030',
        adapter_sequence='AAAGTCTTA',
        flow_cell_barcode='RHFI32',
        # Smart3SeqGenomics
        input_type=Smart3SeqInput.tissue_on_cap,
        number_PCR_cycles=4,
        number_libraries_in_pool=4,
        index_sequence='ACGTAGTTAGTTCGTA',
        indexing_type=Smart3SeqIndexing.dual,
    )
    bs404_1.genomics = [gs111_1]
    gs111_2 = Smart3SeqGenomics(
        labcasID='/to/be/determined/10/2',
        fileName='RNA386_MDA_3493838.fastq',
        dateFileGenerated=datetime.date(2020, 5, 15),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=111,
        submittingInvestigatorID=613,
        processingLevel='processed',
        fileType='fastq',
        # Genomics
        specimen_ID='MCL111_404_10002',
        sequencing_center=111,
        sequencing_date=datetime.date(2020, 5, 15),
        sequencing_batch_id='FCQ3030',
        library_name='BkRNASeq_4902',
        library_strategy=SequencingTechnique.rna_seq,
        library_source=SequencingOrigin.rna,
        library_selection=GenomicMethod.pcr,
        library_strand=GenomicStranding.second_stranded,
        library_layout=False,
        sequencing_platform=GenomicAnalyzer.ab_solid_3,
        read_length=80,
        rin=9,
        adapter_name='B3854',
        adapter_sequence='AAAGGGTTA',
        flow_cell_barcode='DDTY54',
        # Smart3SeqGenomics
        input_type=Smart3SeqInput.rna_in_tube,
        number_PCR_cycles=10,
        number_libraries_in_pool=8,
        index_sequence='AAGGTTCCCTAGCTAG',
        indexing_type=Smart3SeqIndexing.single,
    )
    bs404_2.genomics = [gs111_2]
    gs111_3 = Smart3SeqGenomics(
        labcasID='/to/be/determined/10/3',
        fileName='RNA6844_MDA_32uduus.fastq',
        dateFileGenerated=datetime.date(2020, 5, 15),
        consortium='https://mcl.nci.nih.gov/',
        protocolID=12,
        siteID=111,
        submittingInvestigatorID=613,
        processingLevel='processed',
        fileType='fastq',
        # Genomics
        specimen_ID='MCL111_404_10003',
        sequencing_center=111,
        sequencing_date=datetime.date(2020, 5, 15),
        sequencing_batch_id='FCQ3030',
        library_name='BkRNASeq_4902',
        library_strategy=SequencingTechnique.rna_seq,
        library_source=SequencingOrigin.rna,
        library_selection=GenomicMethod.other,
        library_strand=GenomicStranding.unstranded,
        library_layout=False,
        sequencing_platform=GenomicAnalyzer.ab_solid_3,
        read_length=80,
        rin=10,
        adapter_name='B3854',
        adapter_sequence='AAAGGGTTA',
        flow_cell_barcode='DDTY58',
        # Smart3SeqGenomics
        input_type=Smart3SeqInput.rna_in_tube,
        number_PCR_cycles=12,
        number_libraries_in_pool=8,
        index_sequence='AAGGTTCCCTAGCTTT',
        indexing_type=Smart3SeqIndexing.single,
    )
    bs404_3.genomics = [gs111_3]

    session.add_all([cc1, cc2, cc3, cc4])

    session.commit()


def addTestData(session):
    cc = ClinicalCore(
        participant_ID='XYZ123_456', days_to_consent=123, labcasID='/tmp/data.dat', race=Race.asian,
        anchor_type=Anchors.first_imaging_date, gender=Gender.female, ethnicity=Ethnicity.hispanic,
        education=Education.postgraduate_professional, income=Income.seventy_five_thousand_to_100000,
        age_at_index=22, year_of_birth=1988, height=175, weight=82, prior_cancer=PolarAnswer.yes,
        days_to_weight_recorded=11, current_lesion_type=Lesion.bone, days_to_diagnosis=123, year_of_diagnosis=2017,
        age_at_diagnosis=44, how_detected=Detection.screening, days_to_detection_date=11, days_to_last_screen_date=9,
        days_to_last_neg_screen_date=41, mode_of_detection=Mode.laboratory_test, lesion_type=Neoplasm.metastatic,
        specimen_collected=PolarAnswer.refused, menses_stop=ImpertinentAnswer.not_applicable,
        tobacco_smoking_status=SmokingStatus.former_smoker, biomarker_tested=PolarAnswer.not_reported,
        relative_with_cancer_history=ImpertinentPolarAnswer.unknown, type_tobacco_used=Tobacco.vapor,
        alcohol_history=PolarAnswer.yes,
        prior_lesions=[PriorLesion(lesion_type=Lesion.multiple_myeloma), PriorLesion(lesion_type=Lesion.colon)]
    )
    bs = Biospecimen(
        specimen_ID='XYZ123_456_11', specimen_type=Specimen.aliquot, anatomical_site=AnatomicalSite.lung,
        tumor_tissue_type=TumorTissue.xenograft, precancer_type=Precancers.luad_aah,
        specimen_laterality=Laterality.bilateral, acquisition_method=RulesOfAcquisition.core_biopsy,
        time_excision_to_processing=4, days_to_collection=2, preservation_method=Preserves.o_c_t,
        fixative_used=Fixatives.para_benzoquinone, processing_duration=123, analyte_type=Analytes.repli_g_qiagen_dna,
        storage_method=Storage.frozen_in_liquid_nitrogen, days_to_storage=99, slide_charge_type=SlideCharges.other,
        labcasID='/tmp/more.dat', inscribed_clinicalCore_participant_ID='ZZTOP'
    )
    cc.biospecimens = [bs]
    o1 = BreastOrgan(
        labcasID='/tmp/breast.dat',
        anchor_type=Anchors.highly_suspicious_lesion_imaging_date, grade=Grade.intermediate,
        laterality=Laterality.right, site=BreastSite.nipple, size=123, necrosis=MysteriousPolarAnswer.yes,
        necrosis_location=NecrosisLocation.focal, recurrence=MysteriousPolarAnswer.yes,
        genetic_testing=GeneticTestingAnswer.not_done, brca1=TestResults.positive, brca2=TestResults.negative,
        estrogen_receptor=EstrogenTestResults.low_positive, progesterone_receptor=TestResults.cannot_be_determined,
        her2_immunohistochemistry=HER2Results.positive_score_3_plus, menopausal_status=Menopause.perimenopausal,
        ecog_score=ECOGScore.s3, method_of_detection=BreastCancerDetectionMethod.nipple_discharge,
        days_to_detection_date=99, days_to_last_negative_screening_mammo=12, days_to_last_screening_mammo=13,
        detected_between_screening_intervals=MysteriousPolarAnswer.data_not_available,
        multifocal_disease=MysteriousPolarAnswer.data_not_available, multicentric_disease=MysteriousPolarAnswer.yes,
        imaging_workup=BreastImagingWorkup.ultrasound, birads_density=BIRADSTissues.predominantly_fatty,
        histopathology_precancer_types=[
            HistopathologyPrecancerType(hp_type=PrecancerousHistopathology.dcis_paget_disease),
            HistopathologyPrecancerType(hp_type=PrecancerousHistopathology.dcis_cribiform),
        ]
    )
    o2 = ProstateOrgan(depth_or_whatever=99, labcasID='/vmlinuz')
    o3 = ProstateOrgan(depth_or_whatever=199, labcasID='/vmlinuz2', inscribed_clinicalCore_participant_ID='ZZTOP')
    cc.organs = [o1, o2]
    g1 = Genomics(
        specimen_ID='XYZ123_456_12', sequencing_center=400, sequencing_date=datetime.date(2020, 1, 3),
        sequencing_batch_id='QED1', library_name='Baltimore Public Library',
        library_strategy=SequencingTechnique.rna_seq, library_source=SequencingOrigin.dna,
        library_selection=GenomicMethod.pcr, library_strand=GenomicStranding.first_stranded,
        sequencing_platform=GenomicAnalyzer.ab_solid_4, read_length=6,
        labcasID='/tmp/1.gene'
    )
    g2 = Smart3SeqGenomics(
        specimen_ID='XYZ123_456_13', sequencing_center=822, sequencing_date=datetime.date(1973, 5, 6),
        sequencing_batch_id='QED2', library_name='The Great Library at Alexandria',
        library_strategy=SequencingTechnique.bisulfite_seq, library_source=SequencingOrigin.rna,
        library_selection=GenomicMethod.poly_t_enrichment, library_strand=GenomicStranding.second_stranded,
        sequencing_platform=GenomicAnalyzer.ab_solid_2, read_length=9,
        number_PCR_cycles=7, input_type=Smart3SeqInput.tissue_on_cap, number_libraries_in_pool=7,
        index_sequence='CGTAACT', indexing_type=Smart3SeqIndexing.single,
        labcasID='/tmp/2.gene', inscribed_clinicalCore_participant_ID='ZZTOP', inscribed_biospecimen_specimen_ID='ZZBOT'
    )
    cc.genomics = [g1]
    bs.genomics = [g2]
    i1 = Imaging(labcasID='/tmp/1.png', some_attribute=42)
    i2 = Imaging(
        labcasID='/tmp/2.png', some_attribute=69,
        inscribed_clinicalCore_participant_ID='ZZTOP', inscribed_biospecimen_specimen_ID='ZZBOT'
    )
    cc.images = [i1]
    bs.images = [i2]
    session.add_all([cc, o3])

    # Try out inscribed_clinicalCore_participant_ID:
    organs = session.query(Organ).filter(Organ.inscribed_clinicalCore_participant_ID == 'ZZTOP')
    cc.organs.extend(organs.all())

    session.commit()


def main():
    '''Command-line entrypoint: creates tables and optionally populates with some test data'''
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument('-U', '--username', default='mcl', help='Database username (%(default)s)')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-w', '--no-password', default=True, action='store_true', help="Don't use a database password")
    group.add_argument('-W', '--password', default=False, action='store_true', help='Prompt for a database password')
    parser.add_argument('-H', '--host', default='localhost', help='Database host (%(default)s)')
    parser.add_argument('-d', '--dbname', default='clinical_data', help='Database name (%(default)s)')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Be verbose (%(default)s)')
    parser.add_argument('-a', '--add-test-data', action='store_true', default=False, help='Add test data (%(default)s)')
    parser.add_argument('-s', '--add-sample-data', action='store_true', default=False, help="Add Kristen Anton's sample data (%(default)s)")
    args = parser.parse_args()

    password = None if not args.password else getpass.getpass(f'{args.username} password: ')
    if password:
        url = f'postgresql://{args.username}:{password}@{args.host}/{args.dbname}'
    else:
        url = f'postgresql://{args.username}@{args.host}/{args.dbname}'

    engine = create_engine(url, echo=args.verbose)
    createMetadata(engine)

    if args.add_test_data or args.add_sample_data:
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        if args.add_test_data:
            addTestData(session)
        if args.add_sample_data:
            addSampleData(session)

        for i in session.query(ClinicalCore):
            # Do a JSON dump:
            print(json.dumps(i, cls=ClinicalCoreEncoder))
            # Or just access your favorite attributes:
            # print(i, i.anchor_type, type(i.anchor_type), [j for j in i.genomics], [j for j in i.images])
            # for o in i.organs:
            #     print(json.dumps(o, cls=ORGAN_ENCODERS[o.__class__]))
            # for j in i.biospecimens:
            #     # Try some JSON:
            #     print(json.dumps(j, cls=BiospecimenEncoder))
            #     # Do nested queries:
            #     # print(j, [k for k in j.genomics], [k for k in j.images])


if __name__ == '__main__':
    main()
