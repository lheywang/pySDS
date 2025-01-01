# ============================================================================================================
# Acquisition.py
# lheywang on 19/12/2024
#
# Base file for the acquisition class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase


class SiglentAcquisition(SiglentBase):
    """
    pySDS [Acquision][SiglentAcquisition] :   C lass herited from SiglentBase.
                                                Store all command related to the control of acquision
        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (13):
                Arm :                       Prepare the device to be ready to trigger
                Stop :                      Stop the device to be ready to trigger
                ConfigureAquireMethod :     Configure the way of acquiring data
                SetAverageCount :           Configure the average number of sample
                GetAverageCount :           Get the number of average samples
                GetMemorySize :             Get the size in sample of the memory used
                SetMemorySize :             Configure the size in sample of the memory
                GetAcquisitionStatus :      Return the acquision status
                GetSampleRate :             Return the used sample rate (function of time resolution and channel)
                GetSampleNumber :           Return the number of sample stored
                SetInterpolationMethod :    Configure the interpolation method to be used (only on display, inter points)
                EnableXYMode :              Enable the XY mode
                DisableXYMode :             Disable the XY mode
    """

    def Arm(self):
        """
        pySDS [Acquisition][Arm] : Place the device to be ready to acquire a waveform once a triggering condition has been validated

            Arguments :
                None

            Returns :
                self.GetDeviceStatus()[13] which take 1 if trigger is ready, 0 otherwise
        """
        self.__instr__.write("ARM")
        return self.__baseclass__.GetDeviceStatus()[13]

    def Stop(self):
        """
        pySDS [Acquisition][Stop] : Stop the device to be ready to acquire a waveform.

            Arguments :
                None

            Returns :
                self.GetDeviceStatus()[13] which take 1 if trigger is cancelled, 0 otherwise
        """
        self.__instr__.write("STOP")
        return not self.__baseclass__.GetDeviceStatus[13]

    def ConfigureAquireMethod(self, Method: str, AverageNumber: int = 1):
        """
        pySDS [Acquisition][ConfigureAquireMethod] : Configure the way the device handle data acquisition

            Arguments :
                Method : SAMPLING | PEAK_DETECT | AVERAGE | HIGH_RES
                AverageNumber : Number of sample used to compute an average point

            Returns :
                0 | -1 : The device responded with the same settings or differents one.
        """

        if Method not in ["SAMPLING", "PEAK_DETECT", "AVERAGE", "HIGH_RES"]:
            print(
                "     [ PySDS ] [ Acquisition ] [ ConfigureAquireMethod ] : Invalid aquisition way provided"
            )
            return -2

        self.__instr__.write(f"ACQW {Method},{AverageNumber}")
        return self.__baseclass__.GetAllErrors()

    def SetAverageCount(self, AverageNumber):
        """
        pySDS [Acquisition][SetAverageCount] : Configure the number of sampled used per average

            Arguments :
                AverageNumber : Number of sample used to compute an average point

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"AVGA {AverageNumber}")

        return self.__baseclass__.GetAllErrors()

    def GetAverageCount(self):
        """
        pySDS [Acquisition][GetAverageCount] : Return the number of sample used for averaging

            Arguments :
                None

            Returns :
                Integer : Number of samples
        """
        return int(self.__instr__.write("AVGA?").strip().split(" ")[-1])

    def GetMemorySize(self):
        """
        PySDS [Acquisition][GetMemorySize] : Return the number in millions of samples that can be stored into the memory

        WARNING : The value is expressed in number of samples, and not in bytes !

            Arguments :
                None

            Returns :
                Integer : The number of **MILLIONS** of sample that can be stored
        """
        Ret = self.__instr__.query("MSIZ?")
        return int(Ret.strip().split(" ")[-1][:-1])

    def SetMemorySize(self, value: int):
        """
        PySDS [Acquisition][SetMemorySize] : Set the memory size for the samples of the scope.

        WARNING : The value is expressed in number of samples, and not in bytes !

            Arguments :
                The value in **MILLIONS** to the used.

            Returns :
                self.GetAllErrors() returns (List of errors)
        """
        self.__instr__.write(f"MSIZ {value}M")
        return self.__baseclass__.GetAllErrors()

    def GetAcquisitionStatus(self):
        """
        PySDS [Acquisition][GetAcquisitionStatus] : Return the acquisition status of the device

            Arguments :
                None

            Returns :
                String : Device response
        """

        return self.__instr__.query("SAST?").strip().split(" ")[-1]

    def GetSampleRate(self):
        """
        PySDS [Acquisition][GetSampleRate] : Return the acquisition sample rate that is actually used

            Arguments :
                None

            Returns :
                String : Device response
        """
        return self.__instr__.query("SARA?").strip().split(" ")[-1]

    def GetSampleNumber(self):
        """
        PySDS [Acquisition][GetSampleNumber] : Return the acquisition number of points captured

            Arguments :
                None

            Returns :
                String : Device response
        """
        return self.__instr__.query("SANU?").strip().split(" ")[-1]

    def SetInterpolationMethod(self, Method):
        """
        PySDS [Acquisition][SetInterpolationMethod] :   Configure the interpolation method to be used

            Arguments :
                Method : ON | OFF (sine interpolation or linear interpolation)

            Returns :
                self.GetAllErrors()
        """
        if Method not in ["ON", "OFF"]:
            print(
                "     [ PySDS ] [ Acquisition ] [ SetInterpolationMethod ] : Invalid interpolation method provided"
            )
            return -2

        self.__instr__.write(f"SXSA {Method}")
        return self.__baseclass__.GetAllErrors()

    def EnableXYMode(self):
        """
        PySDS [Acquisition][EnableXYMode] :   Enable the XY mode

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """

        self.__instr__.write("XYDS ON")
        return self.__baseclass__.GetAllErrors()

    def DisableXYMode(self):
        """
        PySDS [Acquisition][DisableXYMode] :    Disable the XY mode

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("XYDS OFF")
        return self.__baseclass__.GetAllErrors()
