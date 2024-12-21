# ============================================================================================================
# Timebase.py
# lheywang on 21/12/2024
#
# Base file for the timebase class
#
# ============================================================================================================

class SiglentTimebase:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass