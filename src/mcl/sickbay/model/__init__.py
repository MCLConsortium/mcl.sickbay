# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

Data model implementation module.
'''


from .base import Base, LabCASMetadata
from .clinicalcore import ClinicalCore, PriorLesion
from .genomics import Genomics, Smart3SeqGenomics
from .images import Imaging
from .organs import Organ, BreastOrgan, ProstateOrgan
from .specimens import Biospecimen, AdjacentSpecimen


def createMetadata(engine):
    '''Make all the known data definitions a reality in the given ``engine``. Note that this requires
    plenty of classes defined by import above.
    '''
    Base.metadata.create_all(engine)


__all__ = [
    AdjacentSpecimen,
    Biospecimen,
    BreastOrgan,
    ClinicalCore,
    createMetadata,
    Genomics,
    Imaging,
    LabCASMetadata,
    Organ,
    PriorLesion,
    ProstateOrgan,
    Smart3SeqGenomics,
]
