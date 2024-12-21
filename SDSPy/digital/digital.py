# ============================================================================================================
# Digital.py
# lheywang on 21/12/2024
#
# Base file for the digital class
#
# ============================================================================================================

class SiglentDigital:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass