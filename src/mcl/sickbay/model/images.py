# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Images of the data model.
'''

from .base import Base, LabCASMetadata
from sqlalchemy import Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import relationship


# Database
# ========

class Imaging(Base, LabCASMetadata):
    '''🖼 Imaging'''

    # Primary key:
    identifier = Column(Integer, Sequence('imaging_id_seq'), primary_key=True)

    # Attributes (TBD):
    some_attribute = Column(Integer)

    # Structural attributes ↓
    inscribed_clinicalCore_participant_ID = Column(String(50))
    inscribed_biospecimen_specimen_ID = Column(String(50))
    # 👆 These are used to look up a detached objects for later association.

    # Relationships:
    clinicalCore_participant_ID = Column(String(50), ForeignKey('clinicalCores.participant_ID'))
    clinicalCore                = relationship('ClinicalCore', back_populates='images')
    biospecimen_specimen_ID     = Column(String(50), ForeignKey('biospecimens.specimen_ID'))
    biospecimen                 = relationship('Biospecimen', back_populates='images')

    # Functions:
    def __repr__(self):
        return f'<{self.__class__.__name__}(identifier={self.identifier})>'

    # Object-relational details:
    __tablename__ = 'images'
