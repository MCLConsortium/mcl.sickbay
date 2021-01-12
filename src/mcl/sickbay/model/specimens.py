# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Biological specimens of the data model.
'''

from .base import Base, LabCASMetadata
from .enums import (
    Specimen, AnatomicalSite, TumorTissue, Laterality, Precancers, RulesOfAcquisition, Preserves, Fixatives,
    Analytes, Storage, SlideCharges, Packaging, Destinations
)
from .genomics import Genomics
from .images import Imaging
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Sequence, Float
from sqlalchemy.orm import relationship


# Database Classes
# ================

class Biospecimen(Base, LabCASMetadata):
    '''🧪 Biological specimen data'''

    # Primary key:
    specimen_ID = Column(String(16), primary_key=True)

    # Attributes:
    specimen_ID_local           = Column(String(25))
    specimen_parent_ID          = Column(String(16))
    specimen_type               = Column(Enum(Specimen, name='specimen_enum'), nullable=False)
    anatomical_site             = Column(Enum(AnatomicalSite, name='anatomical_site_enum'), nullable=False)
    tumor_tissue_type           = Column(Enum(TumorTissue, name='tumor_tissue_enum'), nullable=False)
    precancer_type              = Column(Enum(Precancers, name='precancers_enum'), nullable=False)
    precancer_type_other        = Column(String(100))
    specimen_laterality         = Column(Enum(Laterality, name='laterality_enum'), nullable=False)
    acquisition_method          = Column(Enum(RulesOfAcquisition, name='acquisition_enum'), nullable=False)
    acquisition_method_other    = Column(String(100))
    days_to_collection          = Column(Integer, nullable=False)
    time_excision_to_processing = Column(Integer, nullable=False)
    ischemic_time               = Column(Float)
    portion_weight              = Column(Float)
    total_volume                = Column(Float)
    preservation_method         = Column(Enum(Preserves, name='preserves_enum'), nullable=False)
    preservation_method_other   = Column(String(100))
    fixative_used               = Column(Enum(Fixatives, name='fixatives_enum'), nullable=False)
    fixatives_other             = Column(String(100))
    fixation_duration           = Column(Integer)
    processing_duration         = Column(Integer, nullable=False)
    analyte_type                = Column(Enum(Analytes, name='analytes_enum'), nullable=False)
    analyte_type_other          = Column(String(100))
    protocol_number             = Column(Integer)
    protocol_version            = Column(Integer)
    storage_method              = Column(Enum(Storage, name='storage_enum'), nullable=False)
    storage_method_other        = Column(String(30))
    days_to_storage             = Column(Integer, nullable=False)
    slide_charge_type           = Column(Enum(SlideCharges, name='slide_charges_enum'), nullable=False)
    section_thickness           = Column(Float)
    days_to_shipping            = Column(Integer)
    shipping_conditions         = Column(Enum(Packaging, name='packaging_enum'))
    shipping_destination        = Column(Enum(Destinations, name='destinations_enum'))
    # Note adjacent_specimen_IDs is a 1-to-many relation; see below, captured in attribute "adjacent_specimens"

    # Structural attribute ↓
    inscribed_clinicalCore_participant_ID = Column(String(14))
    # 👆 This is used to look up a detached objects for later assocation.

    # Relationships:
    clinicalCore_participant_ID = Column(String(14), ForeignKey('clinicalCores.participant_ID'))
    clinicalCore                = relationship('ClinicalCore', back_populates='biospecimens')

    # Functions:
    def __repr__(self):
        return f'<{self.__class__.__name__}(specimen_ID={self.specimen_ID})>'

    # Object-relational details:
    __tablename__ = 'biospecimens'


class AdjacentSpecimen(Base):
    '''↖️ Nearby specimens; this is from a ``|``-separated list'''

    # Primary key, an auto-sequenced ID number:
    identifier = Column(Integer, Sequence('adjacent_specimen_id_seq'), primary_key=True)

    # Sole attribute: an adjacent specimen ID
    adjacent_specimen_ID = Column(String(16), nullable=False)

    # Many-to-1 reference to our specimen:
    biospecimen_identifier = Column(String(16), ForeignKey('biospecimens.specimen_ID'))
    biospecimen = relationship('Biospecimen', back_populates='adjacent_specimens')

    # Methods:
    def __repr__(self):
        return f'<{self.__class__.__name__}(identifier={self.identifier})>'

    # Object-relational mapping details:
    __tablename__ = 'adjacentSpecimens'


Biospecimen.adjacent_specimens = relationship(
    'AdjacentSpecimen',
    order_by=AdjacentSpecimen.identifier,
    back_populates='biospecimen'
)


# Additional Relationships
# ------------------------

Biospecimen.genomics = relationship('Genomics', order_by=Genomics.specimen_ID, back_populates='biospecimen')
Biospecimen.images   = relationship('Imaging',  order_by=Imaging.identifier,   back_populates='biospecimen')
