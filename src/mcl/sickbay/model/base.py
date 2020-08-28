# encoding: utf-8


'''MCL Sickbay, a Clinical Data prototype — data model, base definitions'''

from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.ext.declarative import declarative_base


# The "Base" class of all object-relational mapping:
Base = declarative_base(name=__name__)


class LabCASMetadata(object):
    '''👩‍🍳 Mixin metadata from LabCAS for all clinlcal data'''

    # We need at least this so we can link back to the file that produced some clinical data:
    # Why a string of length 2000? Answer: https://stackoverflow.com/questions/417142/
    labcasFileURL = Column(String(2000), nullable=False)

    # This stuff is all recorded in LabCAS itself, so not sure it's needed here 🤷‍♀️
    # Provided just for a sense of completion
    fileName                 = Column(String(255))
    dateFileGenerated        = Column(Date)
    siteID                   = Column(Integer)
    submittingInvestigatorID = Column(Integer)
    processingLevel          = Column(String(16))
    fileType                 = Column(String(32))
