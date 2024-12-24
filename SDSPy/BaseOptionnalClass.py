# ============================================================================================================
# BaseOptionnalClass.py
# lheywang on 17/12/2024
#
# Base class, without real usage except to serve as common base for all options
#
# ============================================================================================================

class SiglentBase:
    """
    pySDS [SiglentBase] : Standard class for all of SCPI subsystems. May be derivated into more specific options, if needed

        Attributes :
            Private (2):
                __instr__ :     Handle to the pyvisa class linked to the device
                __baseclass__   Reference to the base class to get standard functions
            Public (0):
                None

        Methods :
            Private (0):
                None

            Public (0):
                None

        Parents :
            None

        Subclass :
            All of the SCPI substystem class (Acquisition, WGEN...)
            Channel modify __init__.
    """

    def __init__(self, instr, baseclass, number = 0):
        self.__instr__ = instr
        self.__baseclass__ = baseclass