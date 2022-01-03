# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Organs of the data model.
'''

from .base import Base, LabCASMetadata
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Sequence, Float
from sqlalchemy.orm import relationship

from .enums import (
    AdditionalUninvolvedProstateFindings,
    Adenocarcinoma,
    AJCCLocalExtent,
    AJCCMetastasisStage,
    AJCCMetastasisStage8,
    AJCCPathologicStage,
    AJCCProstateInvasionExtent,
    AJCCRegionalLymphInvasionExtent,
    AJCCStaging,
    Anchors,
    BIRADSTissues,
    BreastCancerDetectionMethod,
    BreastImagingWorkup,
    BreastSite,
    BronchialLobe,
    ClinicalMStage7,
    ClinicalMStage8,
    ClinicalNStage7,
    ClinicalNStage8,
    ClinicalTNMCategoryM8,
    ClinicalTNMCategoryN8,
    DuctComms,
    ECOGScore,
    EstrogenTestResults,
    ExocrineStage8,
    GeneticTestingAnswer,
    GleasonGrade,
    GleasonScore,
    Grade,
    GroupStage7,
    GroupStage8,
    HER2InSituHybridization,
    HER2Results,
    HistologyGrading,
    Immunohistochemistry,
    ImmunohistochemistryOutcomes,
    Infiltration,
    IPMNGradeAtExcision,
    IPMNHistologicalSubtypes,
    Laterality,
    LesionFocality,
    LungBiopsy,
    LungBranch,
    LungHistologicType,
    LungLocation,
    LungSegment,
    LymphaticInvasion,
    LypmhLocation,
    MarginalStatus,
    Menopause,
    MicroHistoPathologiclaGrading,
    Mitoses,
    MorphoCytoSubcategories,
    MorpholoCytoSubtypes,
    MysteriousPolarAnswer,
    Necrosis,
    NecrosisLocation,
    NeuroendocrineGroup,
    NoduleLocations,
    PathManagement,
    PathologicMStage7,
    PathologicMStage8,
    PathologicNStage7,
    PolarAnswer,
    PositiveMargins,
    PrecancerousHistopathology,
    PrognosticGroupStage8,
    ProstateHistologicSubtypes,
    ProstateHistology,
    ProstaticNoduleLocations,
    SeminalVesicle,
    TestResults,
    Treatment,
    TStage7,
    TStage8,
    TumorExtent,
    TumorGrade,
    TumorPathologyLocation,
)


# Database Classes
# ================

class Organ(Base, LabCASMetadata):
    '''♥️ This is the base class common to all organs.'''

    # Primary key common to all organs:
    identifier = Column(Integer, Sequence('organ_id_seq'), primary_key=True)

    # Common organ attributes:
    anchor_type = Column(Enum(Anchors, name='anchors_enum'), nullable=False)

    # Note that after telecons with Kristen Anton, we've determined that there are *no*
    # common attributes between organs, save one the *name* of the organ. We capture that
    # below in ``organType``.
    #
    # UPDATE 2021-01-22: ``anchor_type`` appears in the CDEs for all organ-specific data,
    # so that looks pretty common to me! I don't care what Kristen said! 😝
    #
    # Update 2022-01-03: The following appear in both Prostate and Lung now and there seems to be no
    # harm in having them in a common base class:

    ajcc_clinical_m       = Column(Enum(ClinicalMStage7, name='cms7_enum'), nullable=True)
    ajcc_clinical_n       = Column(Enum(ClinicalNStage7, name='cns7_enum'), nullable=True)
    ajcc_clinical_t       = Column(Enum(TStage7, name='ts7_enum'), nullable=True)
    ajcc_clinical_stage   = Column(Enum(GroupStage7, name='group7_enum'), nullable=True)
    ajcc_pathologic_m     = Column(Enum(AJCCMetastasisStage, name='metastasis_enum'), nullable=True)
    ajcc_pathologic_n     = Column(Enum(ClinicalNStage7, name='cns7_enum'), nullable=True)
    ajcc_pathologic_t     = Column(Enum(TStage7, name='ts7_enum'), nullable=True)
    ajcc_pathologic_stage = Column(Enum(AJCCPathologicStage, name='ajccpath_enum'), nullable=True)
    lymph_nodes_tested    = Column(Integer, nullable=True)  # units?
    lymph_node_location   = Column(Enum(LypmhLocation, name='lymph_location_enum'), nullable=True)

    # Structural common attribute ↓
    inscribed_clinicalCore_participant_ID = Column(String(50))
    # 👆 This is used to look up a detached Organ so we can associate it with a ClinicalCore later.

    # Many-to-1 reference to our Clinical Core:
    clinicalCore_participant_ID = Column(String(50), ForeignKey('clinicalCores.participant_ID'))
    clinicalCore = relationship('ClinicalCore', back_populates='organs')

    # Note that histopathology_precancer_types is a 1-to-many relation; see below

    # Common functions:
    def __repr__(self):
        return f'<{self.__class__.__name__}(identifier={self.identifier})>'

    # Object-relational mapping details:
    organType = Column(String(24))  # Inheritiance discriminator
    __mapper_args__ = {'polymorphic_identity': 'organs', 'polymorphic_on': organType}
    __tablename__ = 'organs'


class BreastOrgan(Organ):
    '''💜 Breast: an organ that can get cancer'''

    # Primary key (1–1 with the base class):
    identifier = Column(Integer, ForeignKey('organs.identifier'), primary_key=True)

    # Breast-specific attributes:
    grade                                 = Column(Enum(Grade, name='grade_enum'), nullable=False)
    laterality                            = Column(Enum(Laterality, name='laterality_enum'), nullable=False)
    site                                  = Column(Enum(BreastSite, name='breast_site_enum'), nullable=False)
    size                                  = Column(Integer, nullable=False)
    necrosis                              = Column(Enum(MysteriousPolarAnswer, name='mysterious_enum'), nullable=False)
    necrosis_location                     = Column(Enum(NecrosisLocation, name='necrosis_location_enum'), nullable=False)
    surgical_margin                       = Column(Enum(MarginalStatus, name='marginal_status_enum'))
    recurrence                            = Column(Enum(MysteriousPolarAnswer, name='mysterious_enum'), nullable=False)
    pathologic_T_stage_7                  = Column(Enum(TStage7, name='ts7_enum'))
    pathologic_N_stage_7                  = Column(Enum(PathologicNStage7, name='pns7_enum'))
    pathologic_M_stage_7                  = Column(Enum(PathologicMStage7, name='pms7_enum'))
    clinical_T_stage_7                    = Column(Enum(TStage7, name='ts7_enum'))
    clinical_N_stage_7                    = Column(Enum(ClinicalNStage7, name='cns7_enum'))
    clinical_M_stage_7                    = Column(Enum(ClinicalMStage7, name='cms7_enum'))
    disease_stage_7                       = Column(Enum(GroupStage7, name='group7_enum'))
    path_TNM_class_T_8                    = Column(Enum(TStage8, name='ts8_enum'))
    path_TNM_class_M_8                    = Column(Enum(PathologicMStage8, name='pms8_enum'))
    clinical_TNM_class_T_8                = Column(Enum(TStage8, name='ts8_enum'))
    clinical_TNM_class_N_8                = Column(Enum(ClinicalTNMCategoryN8, name='ctnmc8n_enum'))
    clinical_TNM_class_M_8                = Column(Enum(ClinicalTNMCategoryM8, name='ctnmc8m_enum'))
    disease_stage_ajcc_8                  = Column(Enum(PrognosticGroupStage8, name='progroup8_enum'))
    genetic_testing                       = Column(Enum(GeneticTestingAnswer, name='genetic_testing_enum'), nullable=False)
    brca1                                 = Column(Enum(TestResults, name='test_results_enum'), nullable=False)
    brca2                                 = Column(Enum(TestResults, name='test_results_enum'), nullable=False)
    estrogen_receptor                     = Column(Enum(EstrogenTestResults, name='estrogen_test_enum'), nullable=False)
    er_percent_positivity                 = Column(Integer)  # 🤔 TODO: should this be Float?
    progesterone_receptor                 = Column(Enum(TestResults, name='test_results_enum'), nullable=False)
    her2_immunohistochemistry             = Column(Enum(HER2Results, name='her2_results_enum'), nullable=False)
    her2_in_situ_hybridization            = Column(Enum(HER2InSituHybridization, name='her2_hybrid_enum'))
    ki_67_percent_positive_nuclei         = Column(Integer)  # 🤔 TODO: should this be Float?
    menopausal_status                     = Column(Enum(Menopause, name='menopause_enum'), nullable=False)
    ecog_score                            = Column(Enum(ECOGScore, name='ecogscore_enum'), nullable=False)
    method_of_detection                   = Column(Enum(BreastCancerDetectionMethod, name='bcdm_enum'), nullable=False)
    days_to_detection_date                = Column(Integer, nullable=False)
    days_to_last_screening_mammo          = Column(Integer, nullable=False)
    days_to_last_negative_screening_mammo = Column(Integer, nullable=False)
    detected_between_screening_intervals  = Column(Enum(MysteriousPolarAnswer, name='mysterious_enum'), nullable=False)
    multifocal_disease                    = Column(Enum(MysteriousPolarAnswer, name='mysterious_enum'), nullable=False)
    multicentric_disease                  = Column(Enum(MysteriousPolarAnswer, name='mysterious_enum'), nullable=False)
    imaging_workup                        = Column(Enum(BreastImagingWorkup, name='breast_imaging_workup_enum'), nullable=False)
    birads_density                        = Column(Enum(BIRADSTissues, name='birads_tissues_enum'), nullable=False)

    # Object-relational mapping details:
    __mapper_args__ = {'polymorphic_identity': 'breastOrgans'}
    __tablename__ = 'breastOrgans'


class LungOrgan(Organ):
    '''🫁 Lung-specific data'''

    # Primary key (1–1 with the base class):
    identifier = Column(Integer, ForeignKey('organs.identifier'), primary_key=True)

    # Lung-specific attributes:
    histopathology_precancer_type_other         = Column(String(100))
    collection_method                           = Column(Enum(LungBiopsy, name='lung_biopsy_enum'), nullable=False)
    lymphocytes                                 = Column(Enum(Infiltration, name='infiltration_enum'), nullable=False)
    neutrophils                                 = Column(Enum(Infiltration, name='infiltration_enum'), nullable=False)
    plasma_cells                                = Column(Enum(Infiltration, name='infiltration_enum'), nullable=False)
    macrophages                                 = Column(Enum(Infiltration, name='infiltration_enum'), nullable=False)
    lung_location                               = Column(Enum(LungLocation, name='lung_location_enum'), nullable=False)
    lobe_bronchial_location                     = Column(Enum(BronchialLobe, name='bronchial_llobe_enum'), nullable=False)
    segment                                     = Column(Enum(LungSegment, name='lung_segment_enum'), nullable=False)
    branch                                      = Column(Enum(LungBranch, name='lung_branch_enum'), nullable=False)
    histologic_type                             = Column(Enum(LungHistologicType, name='lung_hist_enum'), nullable=False)
    primary_adenocarcinoma_differentiation_type = Column(Enum(Adenocarcinoma, name='adenocar_enum'), nullable=False)
    tumor_grade                                 = Column(Enum(TumorGrade, name='tumor_grade_enum'), nullable=False)
    ajcc_staging_system_edition                 = Column(Enum(AJCCStaging, name='ajccstaging_enum'), nullable=False)
    ajcc_7_lung_clinical_m                      = Column(Enum(ClinicalMStage7, name='cms7_enum'), nullable=True)
    ajcc_7_lung_clinical_n                      = Column(Enum(ClinicalNStage7, name='cns7_enum'), nullable=True)
    ajcc_7_lung_clinical_t                      = Column(Enum(TStage7, name='ts7_enum'), nullable=True)
    ajcc_7_lung_disease_stage                   = Column(Enum(GroupStage7, name='group7_enum'), nullable=True)
    ajcc_7_lung_pathologic_m                    = Column(Enum(AJCCMetastasisStage, name='metastasis_enum'), nullable=True)
    ajcc_7_lung_pathologic_n                    = Column(Enum(ClinicalNStage7, name='cns7_enum'), nullable=True)
    ajcc_7_lung_pathologic_t                    = Column(Enum(TStage7, name='ts7_enum'), nullable=True)
    ajcc_8_lung_clinical_m                      = Column(Enum(ClinicalMStage8, name='cms8_enum'), nullable=True)
    ajcc_8_lung_clinical_n                      = Column(Enum(ClinicalNStage8, name='cns8_enum'), nullable=True)
    ajcc_8_lung_clinical_t                      = Column(Enum(TStage8, name='ts8_enum'), nullable=True)
    ajcc_8_lung_disease_stage                   = Column(Enum(GroupStage8, name='group8_enum'), nullable=True)
    ajcc_8_lung_pathologic_m                    = Column(Enum(AJCCMetastasisStage8, name='metastasis_enum'), nullable=True)
    ajcc_8_lung_pathologic_n                    = Column(Enum(ClinicalNStage8, name='cns8_enum'), nullable=True)
    ajcc_8_lung_pathologic_t                    = Column(Enum(TStage8, name='ts8_enum'), nullable=True)
    lymph_nodes_positive                        = Column(Integer, nullable=True)
    prior_malignancy                            = Column(Enum(PolarAnswer, name='polar_enum'), nullable=False)
    prior_treatment                             = Column(Enum(Treatment, name='treatment_enum'), nullable=False)

    # Object-relational mapping details:
    __mapper_args__ = {'polymorphic_identity': 'lungOrgans'}
    __tablename__ = 'lungOrgans'


class PancreasOrgan(Organ):
    '''💉 Pancreas-specific data'''

    # Primary key (1–1 with the base class):
    identifier = Column(Integer, ForeignKey('organs.identifier'), primary_key=True)

    # Pancreas-specific attributes:
    histological_grading               = Column(Enum(MicroHistoPathologiclaGrading, enum='yikes_enum'), nullable=False)
    histological_subtypes_ipmn         = Column(Enum(IPMNHistologicalSubtypes, enum='ipnmhs_enum'), nullable=False)
    tumor_pathology_location           = Column(Enum(TumorPathologyLocation, name='tpl_enum'), nullable=False)
    lesion_focality                    = Column(Enum(LesionFocality, name='lf_enum'), nullable=False)
    number_lesions                     = Column(Integer, nullable=False)
    mitotic_rate                       = Column(Enum(Mitoses, name='mitsoses_enum'), nullable=False)
    necrosis                           = Column(Enum(Necrosis, name='necrosis_enum'), nullable=False)
    path_number_of_tumors              = Column(Integer, nullable=False)
    path_tumor_size_largest_lesion     = Column(Float, nullable=False)  # mm
    lesion_size                        = Column(Float, nullable=False)  # mm
    path_ipmn_grade_at_excision        = Column(Enum(IPMNGradeAtExcision, name='ipnmgae_enum'), nullable=False)
    final_path_duct_communication      = Column(Enum(DuctComms, name='ductcomms_enum'), nullable=False)
    path_management_recommendation     = Column(Enum(PathManagement, name='pm_enum'), nullable=False)
    path_acc_num_diag_biopsy           = Column(Integer, nullable=False)
    path_immunohistochemistry          = Column(Enum(Immunohistochemistry, name='immunohistochemistry_enum'), nullable=False)
    path_immunohistochemistry_outcome  = Column(Enum(ImmunohistochemistryOutcomes, name='io_enum'), nullable=False)
    histology_grading                  = Column(Enum(HistologyGrading, name='histologygrading_enum'), nullable=False)
    exocrine_pathologic_T_AJCC_8       = Column(Enum(TStage8, name='ts8_enum'), nullable=False)
    exocrine_pathologic_N_AJCC_8       = Column(Enum(ExocrineStage8, name='es8_enum'), nullable=False)
    exocrine_pathologic_M_AJCC_8       = Column(Enum(ClinicalTNMCategoryM8, name='ctnmc8m_enum'))
    exocrine_clinical_T_AJCC_8         = Column(Enum(TStage8, name='ts8_enum'), nullable=False)
    exocrine_clinical_N_AJCC_8         = Column(Enum(ExocrineStage8, name='es8_enum'), nullable=False)
    exocrine_clinical_M_AJCC_8         = Column(Enum(ClinicalTNMCategoryM8, name='ctnmc8m_enum'))
    exocrine_group_stage_AJCC_8        = Column(Enum(PrognosticGroupStage8, name='progroup8_enum'))
    neuroendocrine_pathologic_T_AJCC_8 = Column(Enum(TStage8, name='ts8_enum'), nullable=False)
    neuroendocrine_pathologic_N_AJCC_8 = Column(Enum(ExocrineStage8, name='es8_enum'), nullable=False)
    neuroendocrine_pathologic_M_AJCC_8 = Column(Enum(AJCCMetastasisStage, name='metastasis_enum'), nullable=False)
    neuroendocrine_clinical_T_AJCC_8   = Column(Enum(TStage8, name='ts8_enum'), nullable=False)
    neuroendocrine_clinical_N_AJCC_8   = Column(Enum(ExocrineStage8, name='es8_enum'), nullable=False)
    neuroendocrine_clinical_M_AJCC_8   = Column(Enum(AJCCMetastasisStage, name='metastasis_enum'), nullable=False)
    neuroendocrine_group_stage         = Column(Enum(NeuroendocrineGroup, name='ng_enum'), nullable=False)

    # Object-relational mapping details:
    __mapper_args__ = {'polymorphic_identity': 'pancreaseOrgans'}
    __tablename__ = 'pancreaseOrgans'


class ProstateOrgan(Organ):
    '''💛 Prostate-specific data'''
    # Primary key (1–1 with the base class):
    identifier = Column(Integer, ForeignKey('organs.identifier'), primary_key=True)

    # Prostate-specific attributes:
    histologic_type                              = Column(Enum(ProstateHistology, name='ph_enum'), nullable=False)
    histologic_subtype                           = Column(Enum(ProstateHistologicSubtypes, name='phs_enum'), nullable=False)
    morphologic_cytologic_subtypes               = Column(Enum(MorpholoCytoSubtypes, name='mcsubtypes_enum'), nullable=False)
    morphologic_cytologic_subcategories          = Column(Enum(MorphoCytoSubcategories, name='mcsubcats_enum'), nullable=False)
    gleason_score_dominant_nodule                = Column(Enum(GleasonScore, name='gleason_score_enum'), nullable=False)
    gleason_grade_group                          = Column(Enum(GleasonGrade, name='gleason_grade_enum'), nullable=False)
    percent_gleason_pattern_4                    = Column(Float)
    tumor_extent                                 = Column(Enum(TumorExtent, name='tumor_extent_enum'), nullable=False)
    location_dominant_nodule                     = Column(Enum(NoduleLocations, name='domloc_enum'), nullable=False)
    location_secondary_nodule                    = Column(Enum(NoduleLocations, name='domloc_enum'), nullable=False)
    local_extent                                 = Column(Enum(AJCCLocalExtent, name='locext_enum'), nullable=False)
    location_extent_extraprostatic_extension     = Column(Enum(ProstaticNoduleLocations, name='long_enum'), nullable=False)
    margins                                      = Column(Enum(MarginalStatus, name='marginal_status_enum'), nullable=False)
    location_nature_positive_margins             = Column(Enum(PositiveMargins, name='positive_margins_enum'), nullable=False)
    summed_length_positive_margin                = Column(Float, nullable=False)  # mm
    highest_grade_at_margin                      = Column(Integer)  # units?
    seminal_vesicle_invasion                     = Column(Enum(SeminalVesicle, name='seminal_vessicle_enum'), nullable=False)
    lymphatic_invasion                           = Column(Enum(LymphaticInvasion, name='lymphatic_invasion_enum', nullable=False))
    pelvic_lymph_nodes                           = Column(Integer)  # units?
    tumor_in_pelvic_lymph_nodes                  = Column(Enum(TestResults, name='test_results_enum'), nullable=False)
    lymph_nodes_metastatic_carcinoma             = Column(Integer)  # units?
    extranodal_extension_identified              = Column(Enum(PolarAnswer, name='polar_enum'), nullable=False)
    ajcc_extent_of_invasion_primary_tumor        = Column(Enum(AJCCProstateInvasionExtent, name='really_long_enum'), nullable=False)
    ajcc_extent_of_invasion_regional_lymph_nodes = Column(Enum(AJCCRegionalLymphInvasionExtent, name='even_longer_enum'), nullable=False)
    ajcc_extent_of_invasion_summary_margins      = Column(Enum(MarginalStatus, name='marginal_status_enum'), nullable=False)
    ajcc_staging_system_edition                  = Column(Enum(AJCCStaging, name='ajccstaging_enum'), nullable=False)
    additonal_findings_uninvolved_prostate       = Column(Enum(AdditionalUninvolvedProstateFindings, name='huge_enum'), nullable=False)
    prior_malignancy                             = Column(Enum(PolarAnswer, name='polar_enum'), nullable=False)
    prior_treatment                              = Column(Enum(Treatment, name='treatment_enum'), nullable=False)

    # Object-relational mapping details:
    __mapper_args__ = {'polymorphic_identity': 'prostateOrgans'}
    __tablename__ = 'prostateOrgans'


class HistopathologyPrecancerType(Base):
    '''🩸 Result of precancerous breast or lung tissue examination; in the spreadsheets submitted to LabCAS,
    this comes from a ``|``-separated list.'''

    # Primary key, an auto-sequenced ID number:
    identifier = Column(Integer, Sequence('histo_precancer_id_seq'), primary_key=True)

    # Attributes of a precancerous histopathology (really it's just the type):
    hp_type = Column(
        Enum(PrecancerousHistopathology, name='precancer_histopath_enum'), nullable=False
    )

    # Many-to-1 reference to our Breast:
    organ_identifier = Column(Integer, ForeignKey('organs.identifier'))
    organ = relationship('Organ', back_populates='histopathology_precancer_types')

    # Methods:
    def __repr__(self):
        return f'<{self.__class__.__name__}(identifier={self.identifier})>'

    # Object-relational mapping details:
    __tablename__ = 'histopathologyPrecancerTypes'


Organ.histopathology_precancer_types = relationship(
    'HistopathologyPrecancerType',
    order_by=HistopathologyPrecancerType.identifier,
    back_populates='organ'
)
