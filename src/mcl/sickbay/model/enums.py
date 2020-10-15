# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Enumerations.
'''

from aenum import Enum


class _CaseInsensitiveEnum(Enum):
    @classmethod
    def _missing_name_(cls, value):
        value = value.lower()
        for member in cls:
            if member.value.lower() == value:
                return member
        return None


class Anchors(_CaseInsensitiveEnum):
    '''Date used as the base from which all other dates within a cohort or dataset are derived'''
    first_positive_biopsy_confirming_diagnosis_date = 'First positive biopsy confirming diagnosis date'
    first_imaging_date                              = 'First imaging date'
    highly_suspicious_lesion_imaging_date           = 'Highly suspicious lesion imaging date'


class Gender(_CaseInsensitiveEnum):
    '''Assemblage of properties that distinguish people on the basis of their societal roles'''
    female       = 'Female'
    male         = 'Male'
    unknown      = 'Unknown'
    unspecified  = 'Unspecified'
    not_reported = 'Not reported'


class Ethnicity(_CaseInsensitiveEnum):
    '''Office of Management and Budget (OMB) ethnic categories'''
    hispanic     = 'Hispanic or Latino'
    not_hispanic = 'Not Hispanic or Latino'
    unknown      = 'Unknown'
    not_reported = 'Not reported'


class Race(_CaseInsensitiveEnum):
    '''OMB race categories'''
    white                                     = 'White'
    american_inidan_or_alaska_native          = 'American Indian or Alaska Native'
    black_or_african_american                 = 'Black or African American'
    asian                                     = 'Asian'
    native_hawaiian_or_other_pacific_islander = 'Native Hawaiian or other Pacific Islander'
    other                                     = 'Other'
    unknown                                   = 'Unknown'
    not_reported                              = 'Not reported'


class VitalStatus(_CaseInsensitiveEnum):
    '''Survival state of a person'''
    alive        = 'Alive'
    dead         = 'Dead'
    unknown      = 'Unknown'
    not_reported = 'Not reported'


class Specimen(_CaseInsensitiveEnum):
    '''Types of specimens collected from human bodies'''
    tissue  = 'Tissue'
    blood   = 'Blood'
    aliquot = 'Aliquot'
    analyte = 'Analyte'


class AnatomicalSite(_CaseInsensitiveEnum):
    '''Where on the body specimens may be collected'''
    breast   = 'Breast'
    lung     = 'Lung'
    pancreas = 'Pancreas'
    prostate = 'Prostate'


class Education(_CaseInsensitiveEnum):
    '''Highest level of education attained'''
    some_high_school          = 'Some high school'
    high_school_graduate      = 'High school graduate'
    post_high_school_training = 'Post high school training'
    some_college              = 'Some college'
    college_graduate          = 'College graduate'
    postgraduate_professional = 'Postgraduate/professional'
    unknown                   = 'Unknown'
    not_reported              = 'Not reported'


class Income(_CaseInsensitiveEnum):
    '''Household income in USD'''
    ten_thousand_to_24999           = '$10,000–$24,999'
    twenty_five_thousand_to_44999   = '$25,000–$44,999'
    forty_five_thousand_to_74999    = '$45,000–$74,999'
    seventy_five_thousand_to_100000 = '$75,000–$100,000'
    greater_than_100000             = 'Greater than $100,000'
    less_than_10000                 = 'Less than $10,000'
    refused                         = 'Refused'
    unknown                         = 'Unknown'
    not_reported                    = 'Not reported'


class PolarAnswer(_CaseInsensitiveEnum):
    '''An answer to a yes/no question with the potential for refusal'''
    yes          = 'Yes'
    no           = 'No'
    unknown      = 'Unknown'
    not_reported = 'Not reported'
    refused      = 'Refused'


class ImpertinentAnswer(_CaseInsensitiveEnum):
    '''An answer to a yes/no question with the potential of being inapplicable'''
    yes            = 'Yes'
    no             = 'No'
    unknown        = 'Unknown'
    not_reported   = 'Not reported'
    not_applicable = 'Not applicable'


class ImpertinentPolarAnswer(_CaseInsensitiveEnum):
    '''The best of both worlds'''
    yes            = 'Yes'
    no             = 'No'
    unknown        = 'Unknown'
    not_reported   = 'Not reported'
    not_applicable = 'Not applicable'
    refused        = 'Refused'


class MysteriousPolarAnswer(_CaseInsensitiveEnum):
    '''An answer to a yes/no question with the potential for saying "I dunno"'''
    yes                = 'Yes'
    no                 = 'No'
    data_not_available = 'Data not available'
    unknown            = 'Unknown'


class Lesion(_CaseInsensitiveEnum):
    '''Disease location of a cyst, lesion, atypical neoplastic cells, etc.'''
    bladder                            = 'Bladder'
    bone                               = 'Bone'
    brain                              = 'Brain'
    breast                             = 'Breast'
    cervix                             = 'Cervix'
    colon                              = 'Colon'
    endometrium                        = 'Endometrium'
    esophagus                          = 'Esophagus'
    gallbladder                        = 'Gallbladder'
    head_and_neck_mouth_nose_throat    = 'Head & neck (mouth, nose, and throat)'
    kidney                             = 'Kidney'
    leukemia                           = 'Leukemia'
    liver                              = 'Liver'
    lung                               = 'Lung'
    lymphoma_including_hodgkins        = 'Lymphoma, including Hodgkins'
    mesothelioma                       = 'Mesothelioma'
    multiple_myeloma                   = 'Multiple myeloma'
    ovary                              = 'Ovary'
    pancreas                           = 'Pancreas'
    prostate                           = 'Prostate'
    rectum                             = 'Rectum'
    skin_melanoma_no_basal_or_squamous = 'Skin (melanoma, no basal or squamous)'
    stomach                            = 'Stomach'
    testis                             = 'Testis'
    thyroid                            = 'Thyroid'
    uterus                             = 'Uterus'
    vagina                             = 'Vagina'
    unknown                            = 'Unknown'
    not_reported                       = 'Not reported'
    not_applicable                     = 'Not applicable'


class Detection(_CaseInsensitiveEnum):
    '''How cancer is being detected'''
    screening                       = 'Screening'
    symptom_driven_patient_detected = 'Symptom driven/Patient detected'
    incidental                      = 'Incidental'


class Mode(_CaseInsensitiveEnum):
    '''Mode of cancer detection'''
    imaging         = 'Imaging'
    physical_exam   = 'Physical exam'
    laboratory_test = 'Laboratory test'


class Neoplasm(_CaseInsensitiveEnum):
    '''Type of malignant neoplasm detected'''
    primary    = 'Primary'
    metastatic = 'Metastatic'


class SmokingStatus(_CaseInsensitiveEnum):
    '''🚬?'''
    current_smoker = 'Current smoker'
    former_smoker  = 'Former smoker'
    never_smoker   = 'Never smoker'
    unknown        = 'Unknown'
    not_reported   = 'Not reported'


class Tobacco(_CaseInsensitiveEnum):
    '''Kinds of 🚬'''
    cigarettes            = 'Cigarettes'
    cigar                 = 'Cigar'
    electronic_cigarettes = 'Electronic cigarettes'
    pipe                  = 'Pipe'
    smokeless_tobacco     = 'Smokeless tobacco'
    vapor                 = 'Vapor'
    other                 = 'Other'
    unknown               = 'Unknown'
    not_reported          = 'Not reported'
    not_applicable        = 'Not applicable'


class PrecancerousHistopathology(_CaseInsensitiveEnum):
    '''Preancerous tissue examination'''
    usual_ductal_hyperplasia_udh    = 'Usual ductal hyperplasia (UDH)'
    atypical_ductal_hyperplasia_adh = 'Atypical ductal hyperplasia (ADH)'
    dcis_paget_disease              = 'DCIS-Paget disease'
    dcis_solid_mosaic_microanicar   = 'DCIS-Solid (mosaic, microanicar)'
    dcis_cribiform                  = 'DCIS-Cribiform'
    dcis_micropapillary             = 'DCIS-Micropapillary'
    dcis_papillary                  = 'DCIS-Papillary'
    dcis_comedo                     = 'DCIS-Comedo'
    dcis_nos                        = 'DCIS, NOS'
    lobular_carcinoma_in_situ_lcis  = 'Lobular carcinoma in situ (LCIS)'


class Grade(_CaseInsensitiveEnum):
    '''College of American Pathologists' (CAP) scale'''
    low                = 'Low'
    intermediate       = 'Intermediate'
    high               = 'High'
    data_not_available = 'Data not available'


class Laterality(_CaseInsensitiveEnum):
    '''Side of the body from which tissue was revemod.'''
    bilateral      = 'Bilateral'
    left           = 'Left'
    right          = 'Right'
    unknown        = 'Unknown'
    not_reported   = 'Not reported'
    not_applicable = 'Not applicable'


class BreastSite(_CaseInsensitiveEnum):
    '''Quadrant or structure from which tissue specimen was removed'''
    upper_outer_quadrant = 'Upper outer quadrant'
    lower_outer_quadrant = 'Lower outer quadrant'
    upper_inner_quadrant = 'Upper inner quadrant'
    lower_inner_quadrant = 'Lower inner quadrant'
    central              = 'Central'
    nipple               = 'Nipple'
    data_not_available   = 'Data not available'


class NecrosisLocation(_CaseInsensitiveEnum):
    '''Lesion presence as determined by histological examination'''
    focal              = 'Focal'
    central            = 'Central'
    unknown            = 'Unknown'
    data_not_available = 'Data not available'


class MarginalStatus(_CaseInsensitiveEnum):
    '''Value, significance, or extent of cutting the edge or border of tissue'''
    equivocal        = 'Equivocal'
    negative_finding = 'Negative finding'
    not_evaluable    = 'Not evaluable'
    positive_finding = 'Positive finding'
    unknown          = 'Unknown'


class TStage7(_CaseInsensitiveEnum):
    '''American Joint Committee on Cancer (AJCC) edition 7's pathological tumor "T Stage"'''
    t0         = 'T0'
    t1         = 'T1'
    t1a        = 'T1a'
    t1b        = 'T1b'
    t1c        = 'T1c'
    t1mi       = 'T1mi'
    t2         = 'T2'
    t3         = 'T3'
    t4         = 'T4'
    t4a        = 'T4a'
    t4b        = 'T4b'
    t4c        = 'T4c'
    t4d        = 'T4d'
    tis        = 'Tis'
    tis_pagets = "Tis (Paget's)"
    tis_lcis   = 'Tis (LCIS)'
    tis_dcis   = 'Tis (DCIS)'
    tx         = 'TX'


class TStage8(_CaseInsensitiveEnum):
    '''American Joint Committee on Cancer (AJCC) edition 8's pathological tumor "T Stage".
    Yes it's similar to stage 7 but with subtle differences.'''
    t0         = 'T0'
    t1         = 'T1'
    t1a        = 'T1a'
    t1b        = 'T1b'
    t1c        = 'T1c'
    t1mi       = 'T1mi'
    t2         = 'T2'
    t3         = 'T3'
    t4         = 'T4'
    t4a        = 'T4a'
    t4b        = 'T4b'
    t4c        = 'T4c'
    t4d        = 'T4d'
    tis        = 'Tis'
    tis_pagets = "Tis (Pagets)"
    tis_dcis   = 'Tis (DCIS)'
    tx         = 'TX'


class PathologicNStage7(_CaseInsensitiveEnum):
    '''American Joint Committee on Cancer (AJCC) edition 7's pathological regional lymph node "N Stage"'''
    pn0           = 'pN0'
    pn0_i_plus    = 'pN0(i+)'
    pn0_i_minus   = 'pN0(i-)'
    pn0_mol_plus  = 'pN0(mol+)'
    pn0_mol_minus = 'pN0(mol-)'
    pn1           = 'pN1'
    pn1a          = 'pN1a'
    pn1b          = 'pN1b'
    pn1c          = 'pN1c'
    pn1mi         = 'pN1mi'
    pn2           = 'pN2'
    pn2a          = 'pN2a'
    pn2b          = 'pN2b'
    pn3           = 'pN3'
    pn3a          = 'pN3a'
    pn3b          = 'pN3b'
    pn3c          = 'pN3c'
    pnx           = 'pNX'


class PathologicMStage7(_CaseInsensitiveEnum):
    '''American Joint Committee on Cancer (AJCC) edition 7's pathological distant metastasis "M Stage".
    Note this vocabualry has only one entry at present.'''
    m1 = 'M1'


class PathologicMStage8(_CaseInsensitiveEnum):
    '''American Joint Committee on Cancer (AJCC) edition 8's pathological distant metastasis "M Category".
    And again, yes, there's just one entry. Sigh.'''
    pm1 = 'pM1'


class ClinicalNStage7(_CaseInsensitiveEnum):
    '''American Joint Committee on Cancer (AJCC) edition 7's clinically assesed "M Stage".'''
    n3c = 'N3c'
    n3b = 'N3b'
    n3a = 'N3a'
    n3  = 'N3'
    n2b = 'N2b'
    n2a = 'N2a'
    n2  = 'N2'
    n1  = 'N1'
    n0  = 'N0'
    nx  = 'NX'


class ClinicalMStage7(_CaseInsensitiveEnum):
    '''American Joint Committee on Cancer (AJCC) edition 7's clinically assessed "M Stage".'''
    m0        = 'M0'
    m1        = 'M1'
    m0_i_plus = 'M0(i+)'


class GroupStage7(_CaseInsensitiveEnum):
    '''American Joint Committee on Cancer (AJCC) edition 7's group stage.'''
    zero          = '0'
    ia            = 'IA'
    ib            = 'IB'
    iia           = 'IIA'
    iib           = 'IIB'
    iiia          = 'IIIA'
    iiib          = 'IIIB'
    iiic          = 'IIIC'
    iv            = 'IV'
    stage_unknown = 'Stage unknown'


class ClinicalTNMCategoryN8(_CaseInsensitiveEnum):
    '''American Joint Committee on Caner (AJCC) edition 8's clinically assessed lymph node N category.'''
    cn0   = 'cN0'
    cn1   = 'cN1'
    cn1mi = 'cN1mi'
    cn2   = 'cN2'
    cn2a  = 'cN2a'
    cn2b  = 'cN2b'
    cn3   = 'cN3'
    n3a   = 'N3a'
    cn3b  = 'cN3b'
    cn3c  = 'cN3c'
    cnx   = 'cNX'


class ClinicalTNMCategoryM8(_CaseInsensitiveEnum):
    '''American Joint Committee on Cancer (AJCC) edition 8's clinically assessed distant metastasis category.'''
    cm0        = 'cM0'
    cm0_i_plus = 'cM0(i+)'
    cm1        = 'cM1'
    pm1        = 'pM1'


class PrognosticGroupStage8(_CaseInsensitiveEnum):
    '''American Joint Committee on Cance (AJCC) edition 8's prognostic group stage'''
    zero = '0'
    la   = 'lA'
    ib   = 'IB'
    iia  = 'IIA'
    iib  = 'IIB'
    iiia = 'IIIA'
    iiic = 'IIIC'
    iv   = 'IV'


class GeneticTestingAnswer(_CaseInsensitiveEnum):
    '''How to answer the question of if genetic testing was done'''
    done               = 'Done'
    not_done           = 'Not done'
    unknown            = 'Unknown'
    data_not_available = 'Data not available'


class TestResults(_CaseInsensitiveEnum):
    '''How to conclude analysis or other test results'''
    positive             = 'Positive'
    negative             = 'Negative'
    not_tested           = 'Not tested'
    unknown              = 'Unknown'
    data_not_available   = 'Data not available'
    cannot_be_determined = 'Data not available'  # Make this an alias because the # of vocabs is out of control


class EstrogenTestResults(_CaseInsensitiveEnum):
    '''Because this test has a slightly different set of answers'''
    positive             = 'Positive'
    low_positive         = 'Low positive'
    negative             = 'Negative'
    cannot_be_determined = 'Cannot be determined'
    not_tested           = 'Not tested'
    data_not_available   = 'Data not available'


class HER2Results(_CaseInsensitiveEnum):
    '''Results of testing human epidermal growth factor receptor 2)'''
    negative_score_0       = 'Negative (Score 0)'
    negative_score_1_plus  = 'Negative (Score 1+)'
    equivocal_score_2_plus = 'Equivocal (Score 2+)'
    positive_score_3_plus  = 'Positive (Score 3+)'
    cannot_be_determined   = 'Cannot be determined'
    not_tested             = 'Not tested'
    data_not_available     = 'Data not available'


class HER2InSituHybridization(_CaseInsensitiveEnum):
    '''The result of HER2 genetic in situ hybridization analysis'''
    negative_not_amplified = 'Negative (not amplified)'
    positive_amplified     = 'Positive (amplified)'
    cannot_be_determined   = 'Cannot be determined'
    not_tested             = 'Not tested'
    pending                = 'Pending'
    unknown                = 'Unknown'
    data_not_available     = 'Data not available'


class Menopause(_CaseInsensitiveEnum):
    '''Menopause'''
    premenopausal      = 'Premenopausal'
    perimenopausal     = 'Perimenopausal'
    postmenopausal     = 'Postmenopausal'
    unknown            = 'Unknown'
    data_not_available = 'Data not available'


class ECOGScore(_CaseInsensitiveEnum):
    '''Eastern Cooperative Oncology Group score'''
    s0                 = '0'
    s1                 = '1'
    s2                 = '2'
    s3                 = '3'
    s4                 = '4'
    s5                 = '5'
    unknown            = 'Unknown'
    data_not_available = 'Data not available'


class BreastCancerDetectionMethod(_CaseInsensitiveEnum):
    '''How breast cancer gets detected'''
    clinical_exam_palpation   = 'Clinical exam (palpation)'
    screening_mammogram       = 'Screening mammogram'
    screening_mri             = 'Screening MRI'
    self_exam                 = 'Self exam'
    nipple_discharge          = 'Nipple discharge'
    other                     = 'Other'
    unknown                   = 'Unknown'


class BreastImagingWorkup(_CaseInsensitiveEnum):
    '''Technology used in visualization of breasts'''
    mammogram                   = 'Mammogram'
    ultrasound                  = 'Ultrasound'
    mri                         = 'MRI'
    pet_ct                      = 'PET/CT'
    ct                          = 'CT'
    multiple_imaging_modalities = 'Multiple imaging modalities'
    data_not_available          = 'Data not available'


class BIRADSTissues(_CaseInsensitiveEnum):
    '''Breast Imaging Reporting and Data System category of the kinds of tissues in a mammogram'''
    predominantly_fatty                = 'Predominantly fatty'
    scattered_fibroglandular_densities = 'Scattered fibroglandular densities'
    heterogeneously_dense              = 'Heterogeneously dense'
    extremely_dense                    = 'Extremely dense'


class SequencingTechnique(_CaseInsensitiveEnum):
    '''Bibiolographic tactics'''
    rna_seq                             = 'RNA-Seq'
    mirna_seq                           = 'miRNA-Seq'
    ncrna_seq                           = 'ncRNA-Seq'
    rna_seq_cage                        = 'RNA-Seq (CAGE)'
    rna_seq_race                        = 'RNA-Seq (RACE)'
    chip_seq                            = 'ChIP-Seq'
    mnase_seq                           = 'MNase-Seq'
    mbd_seq                             = 'MBD-Seq'
    mre_seq                             = 'MRE-Seq'
    bisulfite_seq                       = 'Bisulfite-Seq'
    bisulfite_se_reduced_representation = 'Bisulfite-Se (reduced representation)'
    medip_seq                           = 'MeDIP-Seq'
    dnase_hypersensitivity              = 'Dnase-Hypersensitivity'
    tn_seq                              = 'Tn-Seq'
    faire_seq                           = 'FAIRE-seq'
    selex                               = 'SELEX'
    rip_seq                             = 'RIP-Seq'
    chia_pet                            = 'ChIA-PET'
    wgs                                 = 'WGS'
    wxs                                 = 'WXS'
    validation                          = 'Validation'
    amplicon                            = 'Amplicon'
    other                               = 'Other'


class SequencingOrigin(_CaseInsensitiveEnum):
    '''Where genenomic identification came from'''
    dna           = 'DNA'
    rna           = 'RNA'
    bulk_cells    = 'Bulk cells'
    bulk_nuclei   = 'Bulk nuclei'
    bulk_tissue   = 'Bulk tissue'
    single_cells  = 'Single-cells'
    single_nuclei = 'Single-nuclei'


class GenomicMethod(_CaseInsensitiveEnum):
    '''How genomes get sequenced'''
    hybrid_selection         = 'Hybrid Selection'
    pcr                      = 'PCR'
    affinity_enrichment      = 'Affinity Enrichment'
    poly_t_enrichment        = 'Poly-T Enrichment'
    random                   = 'Random'
    rrna_depletion           = 'rRNA Depletion'
    mirna_size_fractionation = 'miRNA Size Fractionation'
    other                    = 'Other'


class GenomicStranding(_CaseInsensitiveEnum):
    '''How helixes get chosen'''
    unstranded      = 'Unstranded'
    first_stranded  = 'First_Stranded'
    second_stranded = 'Second_Stranded'
    not_applicable  = 'Not Applicable'


class GenomicAnalyzer(_CaseInsensitiveEnum):
    '''Gene analysis platform'''
    gs_flx_titanium              = '454 GS FLX Titanium'
    ab_solid_4                   = 'AB SOLiD 4'
    ab_solid_2                   = 'AB SOLiD 2'
    ab_solid_3                   = 'AB SOLiD 3'
    complete_genomics            = 'Complete Genomics'
    illumina_hiseq_x_ten         = 'Illumina HiSeq X Ten'
    illumina_hiseq_x_five        = 'Illumina HiSeq X Five'
    illumina_genome_analyzer_ii  = 'Illumina Genome Analyzer II'
    illumina_genome_analyzer_iix = 'Illumina Genome Analyzer IIx'
    illumina_hiseq_2000          = 'Illumina HiSeq 2000'
    illumina_hiseq_2500          = 'Illumina HiSeq 2500'
    illumina_hiseq_4000          = 'Illumina HiSeq 4000'
    illumina_miseq               = 'Illumina MiSeq'
    illumina_nextseq             = 'Illumina NextSeq'
    ion_torrent_pgm              = 'Ion Torrent PGM'
    ion_torrent_proton           = 'Ion Torrent Proton'
    ion_torrent_s5               = 'Ion Torrent S5'
    pacbio_rs                    = 'PacBio RS'
    other                        = 'Other'
    unknown                      = 'Unknown'
    not_reported                 = 'Not Reported'


class Smart3SeqInput(_CaseInsensitiveEnum):
    '''Substance used in computational analysis'''
    tissue_on_cap  = 'Tissue on cap'
    tissue_in_tube = 'Tissue in tube'
    rna_in_tube    = 'RNA in tube'


class Smart3SeqIndexing(_CaseInsensitiveEnum):
    '''Type of sequencing method that adds a unique identifier sequence to samples'''
    single = 'Single'
    dual   = 'Dual'
    other  = 'Other'


class TumorTissue(_CaseInsensitiveEnum):
    '''Kind of disease present in the lesion or tumor'''
    premalignant   = 'Premalignant'
    metastatic     = 'Metastatic'
    primary        = 'Primary'
    recurrence     = 'Recurrence'
    nos            = 'NOS'
    xenograft      = 'Xenograft'
    unknown        = 'Unknown'
    not_reported   = 'Not reported'
    not_applicable = 'Not applicable'


class Precancers(_CaseInsensitiveEnum):
    '''Precancers. Yep, precancers.'''
    dcis            = 'DCIS'
    luad_aah        = 'LUAD-AAH'
    luad_ais        = 'LUAD-AIS'
    luad_mia        = 'LUAD-MIA'
    lusc_metaplasia = 'LUSC-Metaplasia'
    lusc_dysplasia  = 'LUSC-Dysplasia'
    lusc_cis        = 'LUSC-CIS'
    panin           = 'PanIN'
    ipmn            = 'IPMN'
    pin             = 'PIN'
    other           = 'Other'
    not_applicable  = 'Not applicable'


class RulesOfAcquisition(_CaseInsensitiveEnum):
    '''DS9 dictated'''
    core_biopsy            = 'Core Biopsy'
    incisional_biopsy      = 'Incisional Biopsy'
    excisional_biopsy      = 'Excisional Biopsy'
    blood_draw             = 'Blood draw'
    surgical_resection     = 'Surgical Resection'
    fine_needle_aspiration = 'Fine needle aspiration'
    autopsy                = 'Autopsy'
    other                  = 'Other'
    unknown                = 'Unknown'
    not_reported           = 'Not reported'
    not_applicable         = 'Not applicable'


class Preserves(_CaseInsensitiveEnum):
    '''How samples are saved'''
    cryopreserved                                        = 'Cryopreserved'
    cryopreservation_in_liquid_nitrogen_dead_tissue      = 'Cryopreservation in liquid nitrogen (dead tissue)'
    cryopreservation_in_dry_ice_dead_tissue              = 'Cryopreservation in dry ice (dead tissue)'
    cryopreservation_of_live_cells_in_liquid_nitrogen    = 'Cryopreservation of live cells in liquid nitrogen'
    formalin_fixed_paraffin_embedded_ffpe                = 'Formalin fixed paraffin embedded (FFPE)'
    formalin_fixed___unbuffered                          = 'Formalin fixed - unbuffered'
    formalin_fixed___buffered                            = 'Formalin fixed - buffered'
    fresh                                                = 'Fresh'
    fresh_dissociated                                    = 'Fresh dissociated'
    fresh_dissociated_and_single_cell_sorted             = 'Fresh dissociated and single cell sorted'
    fresh_dissociated_and_single_cell_sorted_into_plates = 'Fresh dissociated and single cell sorted into plates'
    o_c_t                                                = 'OCT'
    snap_frozen                                          = 'Snap frozen'
    frozen                                               = 'Frozen'
    negative_80_degrees_c                                = '-80 degrees C'
    liquid_nitrogen                                      = 'Liquid nitrogen'
    other                                                = 'Other'
    unknown                                              = 'Unknown'
    not_reported                                         = 'Not reported'


class Fixatives(_CaseInsensitiveEnum):
    '''Chemical process or substance preserving biology'''
    acetone             = 'Acetone'
    alcohol             = 'Alcohol'
    formalin            = 'Formalin'
    glutaraldehyde      = 'Glutaraldehyde'
    oct_media           = 'OCT media'
    rnalater            = 'RNAlater'
    saline              = 'Saline'
    ninety_five_ethanol = '95% Ethanol'
    dimidoester         = 'Dimidoester'
    carbodiimide        = 'Carbodiimide'
    dimethylacetamide   = 'Dimethylacetamide'
    para_benzoquinone   = 'Para-benzoquinone'
    paxgene_tissue      = 'PAXgene Tissue'
    other               = 'Other'
    none                = 'None'
    unknown             = 'Unknown'
    not_recorded        = 'Not recorded'


class Analytes(_CaseInsensitiveEnum):
    '''Substances whose chemical constituents are being identified and measured.'''
    cfdna                                   = 'cfDNA'
    dna                                     = 'DNA'
    ebv_immortalized_normal                 = 'EBV immortalized Normal'
    ffpe_dna                                = 'FFPE DNA'
    ffpe_rna                                = 'FFPE RNA'
    genomeplex_rubicon_amplified_dna        = 'GenomePlex (Rubicon) Amplified DNA'
    repli_g_qiagen_dna                      = 'Repli-G (Qiagen) DNA'
    repli_g_pooled_qiagen_dna               = 'Repli-G Pooled (Qiagen) DNA'
    repli_g_x_quiagen_dna                   = 'Repli-G X (Quiagen) DNA'
    rna                                     = 'RNA'
    total_rna                               = 'Total RNA'
    whole_blood                             = 'Whole blood'
    serum                                   = 'Serum'
    plasma                                  = 'Plasma'
    peripheral_blood_mononuclear_cells_pbmc = 'Peripheral blood mononuclear cells (PBMC)'
    other                                   = 'Other'
    not_applicable                          = 'Not applicable'


class Storage(_CaseInsensitiveEnum):
    '''How speciemns get stored after preservation and before use in a protocol'''
    ambient_temperature       = 'Ambient temperature'
    cut_slide                 = 'Cut slide'
    fresh                     = 'Fresh'
    frozen_at__70c            = 'Frozen at -70C'
    frozen_at__80c            = 'Frozen at -80C'
    frozen_at__150c           = 'Frozen at -150C'
    frozen_in_liquid_nitrogen = 'Frozen in liquid nitrogen'
    frozen_in_vapor_phase     = 'Frozen in vapor phase'
    paraffin_block            = 'Paraffin block'
    rnalater_at_4c            = 'RNAlater at 4C'
    rnalater_at_25c           = 'RNAlater at 25C'
    rnalater_at__20c          = 'RNAlater at -20C'
    other                     = 'Other'


class SlideCharges(_CaseInsensitiveEnum):
    '''Whatever'''
    uncharged      = 'Uncharged'
    charged        = 'Charged'
    other          = 'Other'
    unknown        = 'Unknown'
    not_recorded   = 'Not recorded'
    not_applicable = 'Not applicable'


class Packaging(_CaseInsensitiveEnum):
    '''How specimens were packed'''
    ambient_pack                 = 'Ambient pack'
    cold_pack                    = 'Cold pack'
    ice_pack                     = 'Ice pack'
    dry_ice                      = 'Dry ice'
    liquid_nitrogen              = 'Liquid nitrogen'
    specimen_at_room_temperature = 'Specimen at room temperature'
    other_shipping               = 'Other shipping'
    unknown                      = 'Unknown'
    not_recorded                 = 'Not recorded'


class Destinations(_CaseInsensitiveEnum):
    '''Where speicmens go'''
    broad_institute = 'Broad Institute'
    bu              = 'BU'
    dartmouth       = 'Dartmouth'
    john_hopkins    = 'John Hopkins'
    md_anderson     = 'MD Anderson'
    stanford        = 'Stanford'
    ucdavis         = 'UCDavis'
    ucla            = 'UCLA'
    ucsd            = 'UCSD'
    ucsf            = 'UCSF'
    uvm             = 'UVM'
    vanderbilt      = 'Vanderbilt'
