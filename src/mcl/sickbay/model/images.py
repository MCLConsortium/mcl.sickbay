# encoding: utf-8

'''MCL Sickbay, a clinical data prototype — data model — imaging'''

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

    # Relationships:
    clinicalCore_participant_ID = Column(String(14), ForeignKey('clinicalCores.participant_ID'))
    clinicalCore                = relationship('ClinicalCore', back_populates='images')
    biospecimen_specimen_ID     = Column(String(16), ForeignKey('biospecimens.specimen_ID'))
    biospecimen                 = relationship('Biospecimen', back_populates='images')

    # Functions:
    def __repr__(self):
        return f'<{self.__class__.__name__}(identifier={self.identifier})>'

    # Object-relational details:
    __tablename__ = 'images'
