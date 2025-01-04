# ============================================================================================================
# Cursor.py
# lheywang on 19/12/2024
#
# Base file for the cursor class
#
# ============================================================================================================
from ..BaseOptionnalClass import SiglentBase


class ACAL(SiglentBase):
    def EnableAutomaticCalibration(self):
        """
        PySDS [EnableAutomaticCalibration] :    Enable automatic calibration of the device. (When ? )

        WARNING : This command is only available on some CFL series devices

            Arguments :
                None

            Returns :
                self.GetAllErrors() : List of errors
        """

        self.__instr__.write("ACAL ON")
        return self.__baseclass__.GetAllErrors()

    def DisableAutomaticCalibration(self):
        """
        PySDS [DisableAutomaticCalibration] :    Disable automatic calibration of the device.

        WARNING : This command is only available on some CFL series devices

            Arguments :
                None

            Returns :
                self.GetAllErrors() : List of errors
        """

        self.__instr__.write("ACAL OFF")
        return self.__baseclass__.GetAllErrors()

    def GetAutomaticCalibrationState(self):
        """
        PySDS [GetAutomaticCalibrationState] :   Return the state of the autocalibration

        WARNING : This command is only available on some CFL series devices

            Arguments :
                None

            Returns :
                True | False if enabled | Disabled
        """

        Ret = self.__instr__.write("ACAL?").strip().split(" ")[-1]
        if Ret == "ON":
            return True
        return False
