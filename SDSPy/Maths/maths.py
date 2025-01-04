# ============================================================================================================
# Maths.py
# lheywang on 17/12/2024
#
# Base file for the maths class
#
# ============================================================================================================
from ..BaseOptionnalClass import SiglentBase


class SiglentMaths(SiglentBase):
    """
    pySDS [Files][SiglentMaths] :   Class herited from SiglentBase.
                                    Store all command related the control of maths functions.

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (1) :
                __init__ :                  Small overhide to add one variable

            Public (12):
                DefineMathOperation :       Configure math operation
                EnableMathInvert :          Invert the output
                DisableMathInvert :         De-Invert the output
                SetMathVDIV :               Configure VDIV of math channel
                SetMathVerticalPosition :   Set Math position
                SetFFTCenter :              Set FFT Center
                SetFTTDisplayMode :         Set FFT Display mode
                SetFFTVerticalPosition :    Set FFT Position
                SetFFTVerticalScale :       Set FFT Scale
                SetFFTHorizontalScale :     Set FFT Horizontal scale
                SetFFTVerticalUnit :        Set FFT Unit
                SetFFTWindow :              Set FFT Unit
    """

    def __init__(self, instr, baseclass, number=0):
        """
        Small overhide to add a variable to the class.
        """
        super().__init__(instr, baseclass, number)
        self.__VDIV__ = 0

    def DefineMathOperation(self, Equation):
        """
        pySDS [Maths][DefineMathOperation] : Configure math operation to do.

            Arguments :
                Equation : Human written operation

            Returns :
                self.GetAllErrors()
        """
        # First, check that the operation is valid
        # If a non authorized channel was passed -> Not replaced and trigger a -1
        Eq = (
            Equation.replace("C1", ";")
            .replace("C2", ";")
            .replace("C3", ";")
            .replace("C3", ";")
            .split(";")
        )
        for elem in Eq:
            if elem not in ["+", "-", "*", "/", "FFT", "INTG", "DIFF", "SQRT"]:
                return -1

        self.__instr__.write(f"DEFINE EQN,'{Equation}'")
        return self.__baseclass__.GetAllErrors()

    def EnableMathInvert(self):
        """
        pySDS [Math][EnableMathInvert] : Invert the trace of the math result

            Arguments :
                None

            Returns :
                self.GetAllErrors
        """
        self.__instr__.write("MATH:INVERTSET ON")
        return self.__baseclass__.GetAllErrors()

    def DisableMathInvert(self):
        """
        pySDS [Math][EnableMathInvert] : Disable inversion the trace of the math result

            Arguments :
                None

            Returns :
                self.GetAllErrors
        """
        self.__instr__.write("MATH:INVERTSET OFF")
        return self.__baseclass__.GetAllErrors()

    def SetMathVDIV(self, Unit):
        """
        pySDS [Math][SetMathVDIV] : Configure the vertical scale of the math channel

            Arguments :
                Unit : 500uV | 1mV | 2mV | 5mV | 10mV | 20mV | 50mV | 100mV | 200mV | 500mV | 1V | 2V | 5V | 10V | 20V | 50V | 100V

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid unit
        """

        if Unit not in [
            "500uV",
            "1mV",
            "2mV",
            "5mV",
            "10mV",
            "20mV",
            "50mV",
            "100mV",
            "200mV",
            "500mV",
            "1V",
            "2V",
            "5V",
            "10V",
            "20V",
            "50V",
            "100V",
        ]:
            return [1, -1]

        self.__instr__.write(f"MATH_VERT_DIV {Unit}")
        self.__VDIV__ = Unit
        return self.__baseclass__.GetAllErrors()

    def SetMathVerticalPosition(self, Offset):
        """
        pySDS [Math][SetMathVerticalPosition] : Configure the position of the math

            Arguments :
                Offset : Value in uV / mV / V to be offseted on the math signal

            Returns :
                self.GetAllErrors()
                or
                -1 : Out of range value (for this VDIV)
        """
        if (Offset < (-5 * self.__VDIV__)) or (Offset > (5 * self.__VDIV__)):
            return [1, -1]

        points = (Offset * 5) / self.__VDIV__
        self.__instr__.write(f"MATH_VERT_POS {points}")
        return self.__baseclass__.GetAllErrors()

    def SetFFTCenter(self, Value):
        """
        pySDS [Math][SetFFTCenter] : Configure the FFT Center point

        WARNING : It's not possible to check the value here

            Arguments :
                Value in Hz | kHz | MHz

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"FFTC {Value}")
        return self.__baseclass__.GetAllErrors()

    def SetFTTDisplayMode(self, Mode):
        """
        pySDS [Math][SetFFTDisplayMode] : Configure the mode of display of the FFT

            Arguments :
                Mode : ON | OFF | EXCLU

            Returns :
                self.GetAllErrors()
                or
                -1 : Value not allowed
        """
        if Mode not in ["ON", "OFF", "EXCLU"]:
            return [1, -1]

        self.__instr__.write(f"FFTF {Mode}")
        return self.__baseclass__.GetAllErrors()

    def SetFFTVerticalPosition(self, Offset):
        """
        pySDS [Math][SetFFTVerticalPosition] : Configure the VPOS of the FFT

            Arguments :
                Offset : Value in Volts

            Returns :
                self.GetAllErrors()
                or
                -1 : Out of range value
        """
        self.__instr__.write(f"FFTP {Offset}")
        return self.__baseclass__.GetAllErrors()

    def SetFFTVerticalScale(self, Scale):
        """
        pySDS [Math][SetFFTVerticalScale] : Set the FFT scale

        WARNING : Due to the option of two units, some values may be valid but not for this specific mode. VRMS is more restrictive.

            Arguments :
                Scale : Value to be used

            Returns :
                self.GetAllErrors()
                or
                -1 : Out of range value
        """
        if Scale not in [
            0.001,
            0.002,
            0.005,
            0.01,
            0.02,
            0.05,
            0.1,
            0.2,
            0.5,
            1,
            2,
            5,
            10,
            20,
        ]:
            return [1, -1]

        self.__instr__.write(f"FFTS {Scale}")
        return self.__baseclass__.GetAllErrors()

    def SetFFTHorizontalScale(self, Scale):
        """
        pySDS [Math][SetFFTHorizontalScale] : Set the horizontal division of the FFT trace

        WARNING : It's not possible to check the value here

            Arguments :
                Scale : in Hz | kHz | Mhz with unit

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"FFTT {Scale}")
        return self.__baseclass__.GetAllErrors()

    def SetFFTVerticalUnit(self, Unit):
        """
        pySDS [Math][SetFFTVerticalUnit] : Set the FFT unit. This function shall be called first when configuring FFT

            Arguments :
                Unit : VRMS | DBM | DBVRMS

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Unit
        """
        if Unit not in ["VRMS", "DB", "DBVRMS"]:
            return [1, -1]

        self.__instr__.write(f"FFTU {Unit}")
        return self.__baseclass__.GetAllErrors()

    def SetFFTWindow(self, Window):
        """
        pySDS [Math][SetFFTWindow] : Configure the FFT Window to be used

            Arguments :
                Window : RECT | BLAC | HANN | HAMM | FLATTOP

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Window

        Doc from siglent :
            RECT — Rectangle is useful for transient signals, and signals where there are an integral number of cycles in the time record.
            BLAC — Blackman reduces time resolution compared to the rectangular window, but it improves the capacity to detect smaller impulses due to lower secondary lobes (provides minimal spectral leakage).
            HANN — Hanning is useful for frequency resolution and general purpose use. It is good for resolving two frequencies that are close together, or for making frequency measurements.
            HAMM — Hamming.
            FLATTOP — Flattop is the best for making accurate amplitude measurements of frequency peaks
        """
        if Window not in ["RECT", "BLAC", "HANN", "HAMM", "FLATTOP"]:
            return [1, -1]

        self.__instr__.write(f"FFTW {Window}")
        return self.__baseclass__.GetAllErrors()
