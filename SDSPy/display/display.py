# ============================================================================================================
# Screen.py
# lheywang on 17/12/2024
#
# Base file for the screen management class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase


class SiglentScreen(SiglentBase):
    """
    pySDS [Display][SiglentScreen] :    Class herited from SiglentBase.
                                        Store all command related the control of display.

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (6):
    """

    def EnableScreenInterpolation(self):
        """
        pySDS [Screen][EnableScreenInterpolation] : Enable the drawing of lines between data points

            Arguments :
                None

            Returns :
                True | False : Interpolation has been enabled, or not
        """
        ret = self.__instr__.query("DTJN ON").strip().split(" ")[-1]
        if ret == "ON":
            return True
        return False

    def DisableScreenInterpolation(self):
        """
        pySDS [Screen][DisableScreenInterpolation] : Disable the drawing of lines between data points

            Arguments :
                None

            Returns :
                True | False : Interpolation has been disabled, or not
        """
        ret = self.__instr__.query("DTJN OFF").strip().split(" ")[-1]
        if ret == "OFF":
            return True
        return False

    def SelectGrid(self, Grid):
        """
        pySDS [Screen][SelectGrid] : Select the grid on the display

            Arguments :
                Grid : FULL | HALF | OFF

            Returns :
                True | False : Grid has been set, or no
                A false may also indicate a wrong grid has been passed.
        """
        if Grid not in ["FULL", "HALF", "OFF"]:
            return False

        ret = self.__instr__.query(f"GRDS {Grid}").strip().split(" ")[-1]
        if ret.upper() == Grid:
            return True
        return False

    def SetIntensity(self, Grid, Trace):
        """
        pySDS [Screen][Intensity] : Set intensity of the grid display

            Arguments :
                Grid : Value for the grid. 0 to 100
                Trace : Value for the trace. 0 to 100

            Returns :
                True | False : Parameters was set, or not
                False may also indicate a wrong value
        """
        if Grid < 0 or Grid > 100:
            return False
        if Trace < 0 or Trace > 100:
            return False

        ret = (
            self.__instr__.query(f"INTS GRID,{Grid},TRACE,{Trace}")
            .strip()
            .split(" ")[-1]
            .split(",")
        )
        ret = [ret[1], ret[3]]

        if ret[0] == Trace and ret[1] == Grid:
            return True
        return False

    def ShowMenu(self):
        """
        pySDS [Screen][ShowMenu] : Show the menu on the screen

            Arguments :
                None

            Returns :
                True | False : Menu has been showned
        """
        ret = self.__instr__.query("MENU ON").strip().split(" ")[-1]
        if ret == "ON":
            return True
        return False

    def HideMenu(self):
        """
        pySDS [Screen][HideMenu] : Hide the menu on the screen

            Arguments :
                None

            Returns :
                True | False : Menu has been hidden
        """
        ret = self.__instr__.query("MENU OFF").strip().split(" ")[-1]
        if ret == "OFF":
            return True
        return False

    def ConfigurePersistence(self, Value):
        """
        pySDS [Screen][ConfigurePersistence] : Configure the persistence of the track on the screen

        WARNING : OFF may not be available for all of the models.

            Arguments :
                Value : INFINITE | 1 | 5 | 10 | 30 | (OFF)

            Returns :
                True | False. Value has been set, or not
                False may also indicate a wrong setting.
        """
        if Value not in ["INFINITE", "1", "5", "10", "30", "OFF"]:
            return False

        ret = self.__instr__.query(f"PESU {Value}").strip().split(" ")[-1]
        if ret == f"{Value}":
            return True
        return False
