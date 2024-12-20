# ============================================================================================================
# Channel.py
# lheywang on 17/12/2024
#
# Base file for the channel class
#
# ============================================================================================================


class SiglentChannel:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass
