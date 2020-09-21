# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Database related interations.
'''


from . import VERSION
from .model import createMetadata
from .model.clinicalcore import ClinicalCore, PriorLesion
from .model.specimens import Biospecimen
from .model.genomics import Genomics, Smart3SeqGenomics
from .model.images import Imaging
from .model.organs import BreastOrgan, ProstateOrgan, HistopathologyPrecancerType
from .model.enums import (
    Anchors, Gender, Ethnicity, Race, Specimen, AnatomicalSite, Education, Income, PolarAnswer,
    Lesion, Detection, Mode, Neoplasm, ImpertinentAnswer, SmokingStatus, ImpertinentPolarAnswer,
    Tobacco, PrecancerousHistopathology, Grade, Laterality, BreastSite, MysteriousPolarAnswer, NecrosisLocation,
    GeneticTestingAnswer, TestResults, EstrogenTestResults, HER2Results, Menopause, ECOGScore,
    BreastCancerDetectionMethod, BreastImagingWorkup, BIRADSTissues, SequencingTechnique, SequencingOrigin,
    GenomicMethod, GenomicStranding, GenomicAnalyzer, Smart3SeqInput, Smart3SeqIndexing, TumorTissue,
    Precancers, RulesOfAcquisition, Preserves, Fixatives, Analytes, Storage, SlideCharges, VitalStatus
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .json import ClinicalCoreEncoder, ORGAN_ENCODERS, BiospecimenEncoder
import argparse, getpass, datetime, json


_description = '''Generate and populate some database structures for
prototyping purposes. This assumes you've already got a PostgreSQL database
set up and running with permissions to access it.
'''

__version__ = VERSION


def addSampleData(session):
    cc1 = ClinicalCore(
        # LabCASMetadata
        labcasFileURL='https://mcl-labcas.jpl.nasa.gov/to/be/determined/1',
        fileName='12_78_ClinicalCore_20200624_0_DATA',
        dateFileGenerated=datetime.date(2020, 2, 13),
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
    cc2 = ClinicalCore(
        # LabCASMetadata
        labcasFileURL='https://mcl-labcas.jpl.nasa.gov/to/be/determined/2',
        fileName='12_78_ClinicalCore_20200624_0_DATA',
        dateFileGenerated=datetime.date(2020, 2, 13),
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
    cc3 = ClinicalCore(
        # LabCASMetadata
        labcasFileURL='https://mcl-labcas.jpl.nasa.gov/to/be/determined/3',
        fileName='12_111_ClinicalCore_20200623_0_DATA',
        dateFileGenerated=datetime.date(2020, 5, 28),
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
    cc4 = ClinicalCore(
        # LabCASMetadata
        labcasFileURL='https://mcl-labcas.jpl.nasa.gov/to/be/determined/3',
        fileName='12_111_ClinicalCore_20200623_0_DATA',
        dateFileGenerated=datetime.date(2020, 5, 28),
        siteID=111,
        submittingInvestigatorID=613,
        processingLevel='Processed',
        fileType='Clinical Core',
        # ClinicalCore
        participant_ID='MCL111_400',
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
    session.add_all([cc1, cc2, cc3, cc4])
    session.commit()


def addTestData(session):
    cc = ClinicalCore(
        participant_ID='XYZ123_456', days_to_consent=123, labcasFileURL='file:/tmp/data.dat', race=Race.asian,
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
        labcasFileURL='file:/tmp/more.dat',
    )
    cc.biospecimens = [bs]
    o1 = BreastOrgan(
        labcasFileURL='file:/tmp/breast.dat',
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
    o2 = ProstateOrgan(depth_or_whatever=99, labcasFileURL='file:/vmlinuz')
    cc.organs = [o1, o2]
    g1 = Genomics(
        specimen_ID='XYZ123_456_12', sequencing_center=400, sequencing_date=datetime.date(2020, 1, 3),
        sequencing_batch_id='QED1', library_name='Baltimore Public Library',
        library_strategy=SequencingTechnique.rna_seq, library_source=SequencingOrigin.dna,
        library_selection=GenomicMethod.pcr, library_strand=GenomicStranding.first_stranded,
        sequencing_platform=GenomicAnalyzer.ab_solid_4, read_length=6,
        labcasFileURL='file:/tmp/1.gene'
    )
    g2 = Smart3SeqGenomics(
        specimen_ID='XYZ123_456_13', sequencing_center=822, sequencing_date=datetime.date(1973, 5, 6),
        sequencing_batch_id='QED2', library_name='The Great Library at Alexandria',
        library_strategy=SequencingTechnique.bisulfite_seq, library_source=SequencingOrigin.rna,
        library_selection=GenomicMethod.poly_t_enrichment, library_strand=GenomicStranding.second_stranded,
        sequencing_platform=GenomicAnalyzer.ab_solid_2, read_length=9,
        number_PCR_cycles=7, input_type=Smart3SeqInput.tissue_on_cap, number_libraries_in_pool=7,
        index_sequence='CGTAACT', indexing_type=Smart3SeqIndexing.single,
        labcasFileURL='file:/tmp/2.gene'
    )
    cc.genomics = [g1]
    bs.genomics = [g2]
    i1 = Imaging(labcasFileURL='file:/tmp/1.png', some_attribute=42)
    i2 = Imaging(labcasFileURL='file:/tmp/2.png', some_attribute=69)
    cc.images = [i1]
    bs.images = [i2]
    session.add(cc)
    session.commit()


def demo():
    '''Command-line driven demonstration: creates tables and populates with some test data'''
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
