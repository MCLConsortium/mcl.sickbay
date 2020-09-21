# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Clinical core of the data model.
'''

from .base import Base, LabCASMetadata
from .genomics import Genomics
from .images import Imaging
from .organs import Organ
from .specimens import Biospecimen
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, Sequence
from sqlalchemy.orm import relationship

from .enums import (
    Anchors,
    Detection,
    Education,
    Ethnicity,
    Gender,
    ImpertinentAnswer,
    ImpertinentPolarAnswer,
    Income,
    Lesion,
    Mode,
    Neoplasm,
    PolarAnswer,
    Race,
    SmokingStatus,
    Tobacco,
    VitalStatus,
)


# Database
# ========


class ClinicalCore(Base, LabCASMetadata):
    '''🩺 Core clinical data; this has a 1-to-many relationship with the rest of the world'''

    # Primary key:
    participant_ID = Column(String(14), primary_key=True)

    # Attributes (brace yourself—there's a lot 😮):
    anchor_type                        = Column(Enum(Anchors, name='anchors_enum'), nullable=False)
    days_to_consent                    = Column(Integer)
    days_to_enrollment                 = Column(Integer)
    gender                             = Column(Enum(Gender, name='gender_enum'), nullable=False)
    ethnicity                          = Column(Enum(Ethnicity, name='ethnicity_enum'), nullable=False)
    race                               = Column(Enum(Race, name='race_enum'), nullable=False)
    vital_status                       = Column(Enum(VitalStatus, name='vital_status_enum'))
    days_to_vital_status_reference     = Column(Integer)
    age_at_index                       = Column(Integer, nullable=False)
    days_to_birth                      = Column(Integer)
    year_of_birth                      = Column(Integer, nullable=False)
    education                          = Column(Enum(Education, name='education_enum'), nullable=False)
    income                             = Column(Enum(Income, name='income_enum'), nullable=False)
    height                             = Column(Float, nullable=False)  # centimeters
    days_to_weight_recorded            = Column(Integer, nullable=False)
    weight                             = Column(Float, nullable=False)  # kilograms
    prior_cancer                       = Column(Enum(PolarAnswer, name='polar_enum'), nullable=False)
    current_lesion_type                = Column(Enum(Lesion, name='lesion_enum'), nullable=False)
    days_to_diagnosis                  = Column(Integer, nullable=False)
    year_of_diagnosis                  = Column(Integer, nullable=False)
    age_at_diagnosis                   = Column(Integer, nullable=False)
    how_detected                       = Column(Enum(Detection, name='detection_enum'), nullable=False)
    days_to_detection_date             = Column(Integer, nullable=False)
    days_to_last_screen_date           = Column(Integer, nullable=False)
    days_to_last_neg_screen_date       = Column(Integer, nullable=False)
    mode_of_detection                  = Column(Enum(Mode, name='mode_enum'), nullable=False)
    lesion_type                        = Column(Enum(Neoplasm, name='neoplasm_enum'), nullable=False)
    specimen_collected                 = Column(Enum(PolarAnswer, name='polar_enum'), nullable=False)
    age_at_menses_start                = Column(Integer)
    menses_stop                        = Column(Enum(ImpertinentAnswer, name='impertinent_enum'))
    age_at_menses_stop                 = Column(Integer)
    biomarker_tested                   = Column(Enum(PolarAnswer, name='polar_enum'), nullable=False)
    relative_with_cancer_history       = Column(Enum(ImpertinentPolarAnswer, name='impolar_enum'), nullable=False)
    relative_with_cancer_history_count = Column(Integer)
    tobacco_smoking_status             = Column(Enum(SmokingStatus, name='smoking_status_enum'), nullable=False)
    type_tobacco_used                  = Column(Enum(Tobacco, name='tobacco_enum'), nullable=False)
    tobacco_smoking_onset_age          = Column(Integer)
    tobacco_smoking_quit_age           = Column(Integer)
    years_smoked                       = Column(Integer)
    cigarettes_per_day                 = Column(Integer)
    alcohol_history                    = Column(Enum(PolarAnswer, name='polar_enum'), nullable=False)
    alcohol_drinks_per_day             = Column(Integer)
    alcohol_days_per_week              = Column(Integer)
    # ❕ Note that ``prior_lesion_type`` is 1-to-many, so see the next class, below.

    # Methods (brace yourself—there's just 1 so far 😛)
    def __repr__(self):
        return f'<{self.__class__.__name__}(participant_ID={self.participant_ID})>'

    # Object-relational mapping details:
    __tablename__ = 'clinicalCores'


class PriorLesion(Base):
    '''🩸 Prior lesion suffered by a Clinical Core participant; in the spreadsheets submitted to LabCAS,
    this comes from a ``|``-separated list.'''

    # Primary key, an auto-sequenced ID number:
    identifier = Column(Integer, Sequence('prior_lesion_id_seq'), primary_key=True)

    # Attributes of a lesion (really it's just lesion_type):
    lesion_type = Column(Enum(Lesion, name='lesion_enum'), nullable=False)

    # Many-to-1 reference to our Clinical Core:
    clinicalCore_participant_ID = Column(String(14), ForeignKey('clinicalCores.participant_ID'))
    clinicalCore                = relationship('ClinicalCore', back_populates='prior_lesions')

    # Methods:
    def __repr__(self):
        return f'<{self.__class__.__name__}(identifier={self.identifier})>'

    # Object-relational mapping details:
    __tablename__ = 'priorLesions'


# Additional Relationships
# ------------------------

ClinicalCore.biospecimens  = relationship('Biospecimen',  order_by=Biospecimen.specimen_ID, back_populates='clinicalCore')
ClinicalCore.genomics      = relationship('Genomics',     order_by=Genomics.specimen_ID,    back_populates='clinicalCore')
ClinicalCore.images        = relationship('Imaging',      order_by=Imaging.identifier,      back_populates='clinicalCore')
ClinicalCore.organs        = relationship('Organ',        order_by=Organ.identifier,        back_populates='clinicalCore')
ClinicalCore.prior_lesions = relationship('PriorLesion',  order_by=PriorLesion.identifier,  back_populates='clinicalCore')
