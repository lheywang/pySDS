# ============================================================================================================
# BaseOptionnalClass.py
# lheywang on 17/12/2024
#
# Base class, without real usage except to serve as common base for all options
#
# ============================================================================================================

class SiglentBase:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass