# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Genomics of the data model.
'''

from .base import Base, LabCASMetadata
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Boolean, Float
from sqlalchemy.orm import relationship

from .enums import (
    GenomicAnalyzer,
    GenomicMethod,
    GenomicStranding,
    SequencingOrigin,
    SequencingTechnique,
    Smart3SeqIndexing,
    Smart3SeqInput,
)


# Database
# ========

class Genomics(Base, LabCASMetadata):
    '''🧬 Structure, function, evolution, and mapping of genome data'''

    # Primary key:
    specimen_ID = Column(String(50), primary_key=True)

    # Genomics attributes:
    sequencing_center                = Column(Integer, nullable=False)
    sequencing_date                  = Column(Date, nullable=False)
    sequencing_batch_id              = Column(String(12), nullable=False)
    library_name                     = Column(String(40), nullable=False)
    library_strategy                 = Column(Enum(SequencingTechnique, name='sequencing_technique_enum'), nullable=False)
    library_source                   = Column(Enum(SequencingOrigin, name='sequencing_origin_enum'), nullable=False)
    library_selection                = Column(Enum(GenomicMethod, name='genomic_method_enum'), nullable=False)
    library_strand                   = Column(Enum(GenomicStranding, name='genomic_stranding_enum'), nullable=False)
    library_layout                   = Column(Boolean)
    # Note: there is a mispelling here; we are stuck with "analyzier" 😩
    sequencing_platform              = Column(Enum(GenomicAnalyzer, name='genomic_analyzier_enum'), nullable=False)
    read_length                      = Column(String(10))
    rin                              = Column(Float)  # 🤔 TODO: is this Float or Integer? What the heck even is "R.I.N."?
    adapter_name                     = Column(String(40))
    adapter_sequence                 = Column(String(20))
    flow_cell_barcode                = Column(String(20))
    size_selection_range             = Column(Integer)
    target_capture_kit_target_region = Column(String(50))

    # Structural attributes ↓
    inscribed_clinicalCore_participant_ID = Column(String(50))
    inscribed_biospecimen_specimen_ID = Column(String(50))
    # 👆 These are used to look up a detached objects for later association.

    # Relationships:
    clinicalCore_participant_ID = Column(String(50), ForeignKey('clinicalCores.participant_ID'))
    clinicalCore                = relationship('ClinicalCore', back_populates='genomics')
    biospecimen_specimen_ID     = Column(String(50), ForeignKey('biospecimens.specimen_ID'))
    biospecimen                 = relationship('Biospecimen', back_populates='genomics')

    # Functions:
    def __repr__(self):
        return f'<{self.__class__.__name__}(specimen_ID={self.specimen_ID})>'

    # Object-relational mapping details:
    __tablename__ = 'genomics'
    genomicType = Column(String(24))  # Inheritiance discriminator
    __mapper_args__ = {'polymorphic_identity': 'genomics', 'polymorphic_on': genomicType}


class Smart3SeqGenomics(Genomics):
    '''🧠 A kind of genomics that's smart, tripled, and sequenced'''

    # Primary key (1–1 with the base class):
    specimen_ID = Column(String(50), ForeignKey('genomics.specimen_ID'), primary_key=True)

    # Smart3Seq attributes:
    input_type               = Column(Enum(Smart3SeqInput, name='s3s_input_enum'), nullable=False)
    number_PCR_cycles        = Column(Integer, nullable=False)
    number_libraries_in_pool = Column(Integer, nullable=False)
    index_sequence           = Column(String(30), nullable=False)
    indexing_type            = Column(Enum(Smart3SeqIndexing, name='s3s_index_enum'), nullable=False)
    indexing_type_other      = Column(String(20))

    # Object-relational mapping details:
    __mapper_args__ = {'polymorphic_identity': 'smart3SeqGenomics'}
    __tablename__ = 'smart3SeqGenomics'
