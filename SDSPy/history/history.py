# ============================================================================================================
# History.py
# lheywang on 21/12/2024
#
# Base file for the history class
#
# ============================================================================================================
import datetime

from ..BaseOptionnalClass import SiglentBase


class SiglentHistory(SiglentBase):
    """
    pySDS [History][SiglentHistory] :   Class herited from SiglentBase.
                                        Store all command related the control of history display.

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (7):
                EnableHistory :                 Enable history mode
                DisableHistory :                Disable history mode
                SetCurrentFrame :               Configure current frame
                GetFrameAcquisitionTime :       GetAcquisitionTime for a defined frame
                EnableHistoryList :             Enable List view
                DisableHistoryList :            Disable List view
    """

    def EnableHistory(self):
        """
        pySDS [History][EnableHistory] : Enable the History mode

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("HSMD ON")
        return self.__baseclass__.GetAllErrors()

    def DisableHistory(self):
        """
        pySDS [History][DisableHistory] : Disable the History mode

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("HSMD OFF")
        return self.__baseclass__.GetAllErrors()

    def SetCurrentFrame(self, Number):
        """
        pySDS [History][SetCurrentFrame] : Configure the current frame where the data is stored

            Arguments :
                Number : Integer of the position. Generally between 0 and 7960, but upper value can be influed by hardware options, timebase or resolution.

            Returns :
                self.GetAllErrors() : List of errors
        """
        self.__instr__.write(f"FRAM {Number}")
        return self.__baseclass__.GetAllErrors()

    def GetFrameAcquisitionTime(self):
        """
        pySDS [History][GetFrameAcquisitionTime] : Return the acquision time for this frame

            Arguments :
                None

            Returns :
                Duration under the form of a Python Time object (from Datetime package)
        """

        ret = self.__instr__.query("FTIM?").strip()

        if ret.split(" ")[0] == "FTIM":
            ret = ret.split(" ")[-1].split(":")
            return datetime.time(
                hour=ret[0].strip(),
                minute=ret[1].strip(),
                second=ret[2].strip(),
                microsecond=ret[3].strip(),
            )

        else:
            # Get measurement parameters
            samples = int(ret.replace(r"\x", ""), 16)
            sampling = 1 / int(self.__baseclass__.Acquistion.GetSampleRate()[:-3])

            # Measure duration
            duration = samples * sampling

            return datetime.time(microsecond=duration / 1000)

    def EnableHistoryList(self):
        """
        pySDS [History][EnableHistoryList] : Enable the list mode

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("HSLST ON")
        return self.__baseclass__.GetAllErrors()

    def DisableHistoryList(self):
        """
        pySDS [History][DisableHistoryList] : Disable the list mode

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.query("HSLST OFF")
        return self.__baseclass__.GetAllErrors()
