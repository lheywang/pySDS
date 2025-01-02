# ============================================================================================================
# Files.py
# lheywang on 19/12/2024
#
# Base file for the file management class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase


class SiglentFiles(SiglentBase):
    """
    pySDS [Files][SiglentFiles] :   Class herited from SiglentBase.
                                    Store all command related the control of filesystem.

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (7):
                CaptureBMPScreen :          Capture the screen as a BMP File
    """

    def CaptureBMPScreen(self, File):
        """
        pySDS [Files][CaptureBMPScreen] : Capture the screen and write a BMP file

            Arguments :
                File : Path to be written

            Returns :
                self.GetAllErrors()
        """

        self.__instr__.write("SCDP")
        data = self.__instr__.read_raw()

        with open(File, "wb") as f:
            f.write(data)

        return self.__baseclass__.GetAllErrors()

