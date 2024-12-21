# ============================================================================================================
# History.py
# lheywang on 21/12/2024
#
# Base file for the history class
#
# ============================================================================================================

class SiglentHistory:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass