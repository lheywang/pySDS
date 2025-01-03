# ============================================================================================================
# Screen.py
# lheywang on 17/12/2024
#
# Base file for the screen management class
#
# ============================================================================================================
from ..BaseOptionnalClass import SiglentBase


class SiglentScreen(SiglentBase):
    """
    pySDS [Display][SiglentScreen] :    Class herited from SiglentBase.
                                        Store all command related the control of display.

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (7):
                EnableScreenInterpolation :         Enable continuous display of the tracks
                DisableScreenInterpolation :        Enable the display of only points
                SelectGrid :                        Select the grid type
                SetIntensity :                      Select the trace and grid intensity
                ShowMenu :                          Show menu
                HideMenu :                          Hide menu
                ConfigurePersistence :              Configure trace persistence
    """

    def EnableScreenInterpolation(self):
        """
        pySDS [Screen][EnableScreenInterpolation] : Enable the drawing of lines between data points

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("DTJN ON")
        return self.__baseclass__.GetAllErrors()

    def DisableScreenInterpolation(self):
        """
        pySDS [Screen][DisableScreenInterpolation] : Disable the drawing of lines between data points

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("DTJN OFF")
        return self.__baseclass__.GetAllErrors()

    def SelectGrid(self, Grid):
        """
        pySDS [Screen][SelectGrid] : Select the grid on the display

            Arguments :
                Grid : FULL | HALF | OFF

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid grid mode
        """
        if Grid not in ["FULL", "HALF", "OFF"]:
            return [1, -1]

        self.__instr__.write(f"GRDS {Grid}")
        return self.__baseclass__.GetAllErrors()

    def SetIntensity(self, Grid, Trace):
        """
        pySDS [Screen][Intensity] : Set intensity of the grid display

            Arguments :
                Grid : Value for the grid. 0 to 100
                Trace : Value for the trace. 0 to 100

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid grid value
                -2 : Invalid trace value
        """
        if Grid < 0 or Grid > 100:
            return [1, -1]
        if Trace < 0 or Trace > 100:
            return [1, -2]

        self.__instr__.write(f"INTS GRID,{Grid},TRACE,{Trace}")
        return self.__baseclass__.GetAllErrors()

    def ShowMenu(self):
        """
        pySDS [Screen][ShowMenu] : Show the menu on the screen

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("MENU ON")
        return self.__baseclass__.GetAllErrors()

    def HideMenu(self):
        """
        pySDS [Screen][HideMenu] : Hide the menu on the screen

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("MENU OFF")
        return self.__baseclass__.GetAllErrors()

    def ConfigurePersistence(self, Value):
        """
        pySDS [Screen][ConfigurePersistence] : Configure the persistence of the track on the screen

        WARNING : OFF may not be available for all of the models.

            Arguments :
                Value : INFINITE | 1 | 5 | 10 | 30 | (OFF)

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid persistence value
        """
        if Value not in ["INFINITE", "1", "5", "10", "30", "OFF"]:
            return [1, -1]

        self.__instr__.write(f"PESU {Value}")
        return self.__baseclass__.GetAllErrors()
