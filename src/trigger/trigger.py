# ============================================================================================================
# Trigger.py
# lheywang on 19/12/2024
#
# Base file for the trigger class
#
# ============================================================================================================

class SiglentTrigger:
    def __init__(self, instr):
        self.__instr__ = instr
        

    def SetTriggerCoupling(self):
        pass