# encoding: utf-8

'''MCL Sickbay, a clinical data prototype — data model'''


from .base import Base
from .clinicalcore import ClinicalCore, PriorLesion
from .genomics import Genomics
from .images import Imaging
from .organs import Organ, BreastOrgan, ProstateOrgan
from .specimens import Biospecimen


def createMetadata(engine):
    '''Make all the known data definitions a reality in the given ``engine``. Note that this requires
    plenty of classes defined by import above.
    '''
    Base.metadata.create_all(engine)


__all__ = [
    createMetadata,
    Biospecimen,
    BreastOrgan,
    ClinicalCore,
    Genomics,
    Imaging,
    Organ,
    PriorLesion,
    ProstateOrgan,
]
