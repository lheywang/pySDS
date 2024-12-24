# ============================================================================================================
# Communication.py
# lheywang on 21/12/2024
#
# Base file for the Communication class
#
# ============================================================================================================
from enum import Enum
from BaseOptionnalClass import SiglentBase

CommunicationForms = Enum("Header", [("LONG","LONG"),("SHORT","SHORT"),("OFF","OFF")])

class SiglentCommunication(SiglentBase):
    def SetCommHeader(self, Mode: CommunicationForms):
        """
        SDSpy [Communication][SetCommHeader] :  Configure the used form to answer for the device.

        WARNING :   This function may cause others function to become broken since the parsing from the default answer.
                    LONG / SHORT won't cause issues, the real issue is with OFF where the unit is suppressed. Since the parsing remove the last char, you will end up with power errors !

            Arguments :
                Mode : LONG | SHORT | OFF : The mode of response

            Returns :
                self.GetAllErrors() : List of errors
        """

        if Mode not in CommunicationForms:
            print(
                "     [ PySDS ] [ Communication ] [ SetCommHeader ] : Incorrect mode required"
            )
            return [1, -1]  # Emulate the standard return type
        
        self.__instr__.write(f"COMM_HEADER {Mode}")
        return self.__baseclass__.GetAllErrors()
    
    def GetCommHeader(self):
        """
        SDSpy [Communication][GetCommHeader] :  Return the response form of the device

            Arguments :
                None

            Returns :
                String : The mode of operation
        """

        return self.__instr__.query("COMM_HEADER?").strip().split(" ")[-1]
