# ============================================================================================================
# References.py
# lheywang on 21/12/2024
#
# Base file for the reference class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel


class SiglentReference(SiglentBase):
    """
    pySDS [Files][SiglentReference] :   Class herited from SiglentBase.
                                        Store all command related the control of reference channel selection

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (8):
            CloseReference :                Close the reference functions package
            EnableDisplayOfReference :      Enable display
            DisableDisplayOfReference :     Disable display
            SetReferenceLocation :          Set location of the reference (A, B, C, D)
            SetReferenceOffset :            Set reference offset
            SaveWaveformAsReference :       Save waveform as reference
            SetReferenceScale :             Set reference scale
            SetReferenceSource :            Set reference source
    """

    def CloseReference(self):
        """
        pySDS [Reference][CloseReference] : Close the reference function on the device

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("REFCL")
        return self.__baseclass__.GetAllErrors()

    def EnableDisplayOfReference(self):
        """
        pySDS [Reference][EnableDisplayOfReference] : Display the used reference on the screen

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("REFDS ON")
        return self.__baseclass__.GetAllErrors()

    def DisableDisplayOfReference(self):
        """
        pySDS [Reference][DisableDisplayOfReference] : Hide the used reference on the screen

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("REFDS OFF")
        return self.__baseclass__.GetAllErrors()

    def SetReferenceLocation(self, Location):
        """
        pySDS [Reference][SetReferenceLocation] : Set the location of the actual reference

            Arguments :
                Location : A | B | C | D

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid location
        """
        if Location not in ["A", "B", "C", "D"]:
            return [1, -1]

        self.__instr__.write(f"REFLA REF{Location}")
        return self.__baseclass__.GetAllErrors()

    def SetReferenceOffset(self, Offset):
        """
        pySDS [Reference][SetReferenceOffset] : Apply an offset on the reference display

            Arguments :
                Offset : The offset in volts

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"REFPO {Offset}V")
        return self.__baseclass__.GetAllErrors()

    def SaveWaveformAsReference(self):
        """
        pySDS [Reference][SaveWaveformAsReference] : Save the current channel source on the current reference location

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("REFSA")
        return self.__baseclass__.GetAllErrors()

    def SetReferenceScale(self, Scale):
        """
        pySDS [Reference][SetReferenceScale] : Set the display reference scale

            Arguments :
                Scale : The unit in volts (500uV - 10V)

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid scale
        """
        if Scale < 0.000_5 or Scale > 10:
            return [1, -1]

        self.__instr__.write(f"REFSC {Scale}V")
        return self.__baseclass__.GetAllErrors()

    def SetReferenceSource(self, Channel: SiglentChannel):
        """
        pySDS [Reference][SetReferenceSource] : Set the reference channel to be used

            Arguments :
                Channel : SiglentChannel to be used (or MATH)

            Returns :
                self.GetAllErrors()
        """

        if Channel == "MATH":
            self.__instr__.write("REFSR MATH")
        else:
            self.__instr__.write(f"REFSR {Channel.__channel__}")
        return self.__baseclass__.GetAllErrors()
