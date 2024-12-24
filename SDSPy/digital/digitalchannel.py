# ============================================================================================================
# Digital.py
# lheywang on 21/12/2024
#
# Base file for the digital class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase


class SiglentDChannel(SiglentBase):
    def __init__(self, instr, baseclass, channel):
        """
        Overhide the standard class init to store some more advanced data !

        Check SiglentBase doc before !

        Added attributes :
            Private (1) :
                __channel__ :   Descriptor of the channel

            Public (0) :
                None

        Added methods :
            Private (0) :
                None

            Public (0) :
                None
        """
        super().__init__(instr, baseclass)
        self.__channel__ = channel
