# ============================================================================================================
# Auotest.py
# lheywang on 17/12/2024
#
# Base file for the automated test API
#
# ============================================================================================================


class SiglentAutotest:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass
