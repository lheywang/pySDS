# ============================================================================================================
# Channel.py
# lheywang on 17/12/2024
#
# Base file for the channel class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase


class SiglentChannel(SiglentBase):
    """
    pySDS [Channel][SiglentChannel] :   Class herited from SiglentBase.
                                        Store all command related to a channel
        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (12):
                SetAttenuation :            Configure channel attenuation
                EnableBandwithFilter :      Enable 20 MHz filter on the channel
                DisableBandwithFilter :     Disable 20 MHz filter on the channel
                SetCoupling :               Configure channel coupling
                SetOffset :                 Configure channel offset
                SetSkew :                   Configure channel skew
                EnableTrace :               Enable trace draw on the screen
                DisableTrace :              Disable trace draw on the screen
                SetTraceUnit :              Configure trace unit
                SetTraceDIV :               Configure trace gain
                EnableTraceInvert :         Enable inversion of the trace
                DisableTraceInvert :        Disable inversion of the trace
    """

    def __init__(self, instr, baseclass, channel, impedance):
        """
        Overhide the standard class init to store some more advanced data !

        Check SiglentBase doc before !

        Added attributes :
            Private (2) :
                __channel__ :   Descriptor of the channel
                __impedance__ : List of supported impedance for this channel

            Public (0) :
                None

        Added methods :
            Private (0) :
                None

            Public (0) :
                None
        """
        super().__init__(instr, baseclass)
        self.__channel__ = channel
        self.__impedance__ = impedance

    def SetAttenuation(self, Value):
        """
        pySDS [Channel][SetAttenuation] : Configure the probe attenuation

            Arguments :
                Value : The attenuation value, between 0.1 and 10000 (checked against a list of values)

            Returns :
                self.GetAllErrors()
        """
        if Value not in [
            0.1,
            0.2,
            0.5,
            1,
            2,
            5,
            10,
            20,
            50,
            100,
            200,
            500,
            1000,
            2000,
            5000,
            10000,
        ]:
            return -1

        self.__instr__.write(f"{self.__channel__}:ATTN {Value}")
        return self.__baseclass__.GetAllErrors()

    def EnableBandwithFilter(self):
        """
        pySDS [Channel][EnableBandwithFilter] : Enable a 20 Mhz low pass filter on the channel. Used to rejet high frequency noise.

            Arguments :
                None__

            Returns :
                self.GetAllErrors()
        """

        self.__instr__.write(f"BWL {self.__channel__},ON")
        return self.__baseclass__.GetAllErrors()

    def DisableBandwithFilter(self):
        """
        pySDS [Channel][DisableBandwithFilter] : Disable a 20 Mhz low pass filter on the channel.

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"BWL {self.__channel__},OFF")
        return self.__baseclass__.GetAllErrors()

    def SetCoupling(self, ACDC="D", Impedance=1000000):
        """
        pySDS [Channel][SetCoupling] : Set the channel coupling mode.

            Arguments :
                ACDC : Mode of coupling, AC or DC (AC rejet any DC signal). Values are A | D
                Impedance : Impedance of input. Warning : Some device doesn't support de 50 Ohm coupling !

            Returns :
                self.GetAllErrors()
                or
                "-1" : Incorrect coupling
                "-2" : Incorrect impedance
        """
        if ACDC not in ["A", "D"]:
            return "-1"

        if Impedance not in self.__impedance__:
            return "-2"

        intimp = "50" if Impedance == 50 else "1M"
        self.__instr__.write(f"{self.__channel__}:CPL {ACDC}{intimp}")

        return self.__baseclass__.GetAllErrors()

    def SetOffset(self, Offset: float):
        """
        pySDS [Channel][SetOffset] : Configure the offset used.

            Arguments :
                Offset, in volts

            Returns :
                self.GetAllErrors()
        """

        self.__instr__.write(f"{self.__channel__}:OFST {Offset}V")
        return self.__baseclass__.GetAllErrors()

    def SetSkew(self, Skew: int):
        """
        pySDS [Channel][SetSkew] : Configure the delay between each channels, to compensate cable lenght matching

            Arguments :
                Skew : +- 100 ns to be applied

            Returns :
                self.GetAllErrors()
                or
                [1, -1] if Skew is not valid !
        """
        if Skew < 100 or Skew > 100:
            return [1, -1]  # Emulate error code !

        self.__instr__.write(f"{self.__channel__}:SKEW {Skew}")
        return self.__baseclass__.GetAllErrors()

    def EnableTrace(self):
        """
        pySDS [Channel][EnableTrace] : Enable the draw of the trace on the screen

            Arguments :
                None

            Return :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{self.__channel__}:TRA ON")
        return self.__baseclass__.GetAllErrors()

    def DisableTrace(self):
        """
        pySDS [Channel][EnableTrace] : Disable the draw of the trace on the screen

            Arguments :
                None

            Return :
                self.GetAllErrors()
        """
        self.__instr__.query(f"{self.__channel__}:TRA OFF")
        return self.__baseclass__.GetAllErrors()

    def SetTraceUnit(self, Unit: str):
        """
        pySDS [Channel][SetTraceUnit] : Configure if the trace is on V (Volt) or A (Ampere)

            Arguments :
                Unit : V | A

            Returns :
                self.GetAllErrors()
        """

        self.__instr__.query(f"{self.__channel__}:UNIT {Unit}")
        return self.__baseclass__.GetAllErrors()

    def SetTraceDIV(self, Div: float):
        """
        pySDS [Channel][SetTraceVDIV] : Configure the gain on the unit of the trace, from 500E-6 to 10

            Arguments :
                Div : Gain to be applied

            Returns :
                self.GetAllErrors()
                or
                or -1 if invalid value
        """
        if Div < 0.000_5 or Div > 10:
            return -1

        self.__instr__.query(f"{self.__channel__}:VDIV {Div}")
        return self.__baseclass__.GetAllErrors()

    def EnableTraceInvert(self):
        """
        pySDS [Channel][EnableTraceInvert] : Enable invert the measure of the trace (* -1)

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.query(f"{self.__channel__}:INVS ON")
        return self.__baseclass__.GetAllErrors()

    def DisableTraceInvert(self):
        """
        pySDS [Channel][DisableTraceInvert] : Disable invert the measure of the trace (* -1)

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.query(f"{self.__channel__}:INVS OFF")
        return self.__baseclass__.GetAllErrors()
