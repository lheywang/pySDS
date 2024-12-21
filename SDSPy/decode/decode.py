# ============================================================================================================
# Decode.py
# lheywang on 21/12/2024
#
# Base file for the decode class
#
# ============================================================================================================

class SiglentDecode:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass