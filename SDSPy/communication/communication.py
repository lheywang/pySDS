# ============================================================================================================
# Communication.py
# lheywang on 21/12/2024
#
# Base file for the Communication class
#
# ============================================================================================================
from ..BaseOptionnalClass import SiglentBase


class SiglentCommunication(SiglentBase):
    """
    pySDS [Communication][SiglentCommunication] :   Class herited from SiglentBase.
                                                    Store all command related to the communication bus
        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (2):
                SetCommHeader :      Configure the form of response of the device
                GetCommHeader :      Return the form of response of the device
    """

    def SetCommHeader(self, Mode: str):
        """
        SDSpy [Communication][SetCommHeader] :  Configure the used form to answer for the device.

        WARNING :   This function may cause others function to become broken since the parsing from the default answer.
                    LONG / SHORT won't cause issues, the real issue is with OFF where the unit is suppressed. Since the parsing remove the last char, you will end up with power errors !

            Arguments :
                Mode : LONG | SHORT | OFF : The mode of response

            Returns :
                self.GetAllErrors() : List of errors
        """

        if Mode not in ["LONG", "SHORT", "OFF"]:
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
