# ============================================================================================================
# Screen.py
# lheywang on 17/12/2024
#
# Base file for the screen management class
#
# ============================================================================================================


class SiglentScreen:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass
