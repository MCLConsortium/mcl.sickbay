# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Organs of the data model.
'''

from .base import Base, LabCASMetadata
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Sequence
from sqlalchemy.orm import relationship

from .enums import (
    Anchors,
    BIRADSTissues,
    BreastCancerDetectionMethod,
    BreastImagingWorkup,
    BreastSite,
    ClinicalMStage7,
    ClinicalNStage7,
    ClinicalTNMCategoryM8,
    ClinicalTNMCategoryN8,
    ECOGScore,
    EstrogenTestResults,
    GeneticTestingAnswer,
    Grade,
    GroupStage7,
    HER2InSituHybridization,
    HER2Results,
    Laterality,
    MarginalStatus,
    Menopause,
    MysteriousPolarAnswer,
    NecrosisLocation,
    PathologicMStage7,
    PathologicMStage8,
    PathologicNStage7,
    PrecancerousHistopathology,
    PrognosticGroupStage8,
    TestResults,
    TStage7,
    TStage8,
)


# Database Classes
# ================

class Organ(Base, LabCASMetadata):
    '''♥️ This is the base class common to all organs.'''

    # Primary key common to all organs:
    identifier = Column(Integer, Sequence('organ_id_seq'), primary_key=True)

    # If there are any attributes common to all organs, put them here:
    #  «here»
    # Note that after telecons with Kristen Anton, we've determined that there are *no*
    # common attributes between organs, save one the *name* of the organ. We capture that
    # below in ``organType``.

    # Structurally, though, we do have this common attribute ↓
    inscribed_clinicalCore_participant_ID = Column(String(14))
    # 👆 This is used to look up a detached Organ so we can associate it with a ClinicalCore later.

    # Many-to-1 reference to our Clinical Core:
    clinicalCore_participant_ID = Column(String(14), ForeignKey('clinicalCores.participant_ID'))
    clinicalCore = relationship('ClinicalCore', back_populates='organs')

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
    anchor_type                           = Column(Enum(Anchors, name='anchors_enum'), nullable=False)
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
    # Note that histopathology_precancer_types is a 1-to-many relation; see below

    # Object-relational mapping details:
    __mapper_args__ = {'polymorphic_identity': 'breastOrgans'}
    __tablename__ = 'breastOrgans'


class HistopathologyPrecancerType(Base):
    '''🩸 Result of precancerous breast tissue examination; in the spreadsheets submitted to LabCAS,
    this comes from a ``|``-separated list.'''

    # Primary key, an auto-sequenced ID number:
    identifier = Column(Integer, Sequence('histo_precancer_id_seq'), primary_key=True)

    # Attributes of a precancerous histopathology (really it's just the type):
    hp_type = Column(
        Enum(PrecancerousHistopathology, name='precancer_histopath_enum'), nullable=False
    )

    # Many-to-1 reference to our Breast:
    breastOrgan_identifier = Column(Integer, ForeignKey('breastOrgans.identifier'))
    breastOrgan = relationship('BreastOrgan', back_populates='histopathology_precancer_types')

    # Methods:
    def __repr__(self):
        return f'<{self.__class__.__name__}(identifier={self.identifier})>'

    # Object-relational mapping details:
    __tablename__ = 'histopathologyPrecancerTypes'


BreastOrgan.histopathology_precancer_types = relationship(
    'HistopathologyPrecancerType',
    order_by=HistopathologyPrecancerType.identifier,
    back_populates='breastOrgan'
)


class ProstateOrgan(Organ):
    '''💛 Prostate-specific data'''
    # Primary key (1–1 with the base class):
    identifier = Column(Integer, ForeignKey('organs.identifier'), primary_key=True)

    # Prostate-specific attributes:
    depth_or_whatever = Column(Integer)

    # Object-relational mapping details:
    __mapper_args__ = {'polymorphic_identity': 'prostateOrgans'}
    __tablename__ = 'prostateOrgans'
