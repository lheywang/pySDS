# ============================================================================================================
# Measure.py
# lheywang on 21/12/2024
#
# Base file for the measure class
#
# ============================================================================================================

class SiglentMeasure:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass