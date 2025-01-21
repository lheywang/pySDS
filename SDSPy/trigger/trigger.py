# ============================================================================================================
# Trigger.py
# lheywang on 19/12/2024
#
# Base file for the trigger class
#
# ============================================================================================================
from ..BaseOptionnalClass import SiglentBase

from .IIC import SiglentIIC
from .SPI import SiglentSPI
from .CAN import SiglentCAN
from .UART import SiglentUART
from .LIN import SiglentLIN


class SiglentTrigger(SiglentBase):
    """
    pySDS [Files][SiglentTrigger] : Class herited from SiglentBase.
                                    Store all command related the control of the triggering system

                                    Due to advanced features available, this class group subclasses.
                                    Thus, it's possible to trigger on serial busses for a specific address or conditions.

    WARNING : Advanced features are linked to bus decoding ability, and can sometimes interfer between their configurations !

        Attributes :
            Herited from SiglentBase
            +
            I2C (SiglentIIC Class), specified for I2C operation
            SPI (SiglentSPI Class), specified for SPI operation
            LIN (SiglentLIN Class), specified for LIN operation
            SERIAL (SiglentUART Class), specified for UART operation
            CAN (SiglentCAN Class), specified for CAN Operation

        Methods :
            Private (0) :
                None

            Public (15):
                SetCoupling :   Configure trigger coupling
                SetDelay :      Configure trigger delay
                GetDelay :      Get trigger delay
                SetLevel1 :     Set threshold 1
                SetLevel2 :     Set threshold 2
                SetMode :       Set trigger mode
                GetMode :       Get trigger mode
                SetSelect :     Set select
                GetSelect :     Get trigger select
                SetSlope :      Set trigger slope
                GetSlope :      Get trigger slope
                SetWindow :     Set trigger Window
                GetWindow :     Get trigger Window
                SetPattern :    Set trigger pattern
                GetPattern :    Get trigger pattern
    """

    def __init__(self, instr, baseclass, number=0):
        """
        Overhide the standard class init to store some more advanced data !

        Check SiglentBase doc before !

        Added attributes :
            Private (0) :

            Public (0) :
                I2C (SiglentIIC Class), specified for I2C operation
                SPI (SiglentSPI Class), specified for SPI operation
                LIN (SiglentLIN Class), specified for LIN operation
                SERIAL (SiglentUART Class), specified for UART operation
                CAN (SiglentCAN Class), specified for CAN Operation

        Added methods :
            Private (0) :
                None

            Public (0) :
                None
        """
        # Calling default init
        super().__init__(instr, baseclass, number)

        # Creating new members, which are also herited from the base class
        self.I2C = SiglentIIC(instr, baseclass, number)
        self.SPI = SiglentSPI(instr, baseclass, number)
        self.LIN = SiglentLIN(instr, baseclass, number)
        self.CAN = SiglentCAN(instr, baseclass, number)
        self.Serial = SiglentUART(instr, baseclass, number)

        return

    #
    #   COUPLING
    #

    def SetCoupling(self, Channel, Mode):
        """
        PySDS [Trigger][SetCoupling] :  Configure the source and coupling of the trigger

        WARNING : The command to know the state of the trigger hasn't been developped since it suppose we know the channel used...

            Arguments :
                Channel : C1 | C2 | C3 | C4 | EX | EX5 | LINE : You can pass a member of the ENUM TriggerSources, or it's string. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
                Mode : AC | DC | HFREF | LFREJ : You can pass a member of the ENUM TriggerModes or it's name direcly

            Returns :
                self.GetAllErrors() : List of errors
        """
        if Channel not in ["C1", "C2", "C3", "C4", "EX", "EX5", "LINE"]:
            return [1, -1]  # Emulate the standard return type

        if Mode not in ["AC", "DC", "HFREJ", "LFREJ"]:
            return [1, -2]  # Emulate the standard return type

        self.__instr__.write(f"{Channel.__channel__}:TRCP {Mode}")
        return self.__baseclass__.GetAllErrors()

    #
    #   DELAY
    #

    def SetDelay(self, Delay: float):
        """
        PySDS [Trigger][SetDelay] :  Configure the delay (may be positive or negatives)* between the trigger and the first acquistion

        WARNING : Positive delay are only supported on some devices.

            Arguments :
                Delay : The delay in ms to apply

            Returns :
                self.GetAllErrors() : List of errors
        """
        self.__instr__.write(f"TRDL {Delay}ms")
        return self.__baseclass__.GetAllErrors()

    def GetDelay(self):
        """
        PySDS [Trigger][GetDelay] :  Read the delay applied between trigger and acquisition

            Arguments :
                None

            Returns :
                Float : The number of ms of delay
        """
        return float(self.__instr__.query("TRDL?").strip().split(" ")[-1][:-1]) * 1000

    #
    #   LEVEL
    #

    def SetLevel1(self, Channel, Value: float):
        """
        PySDS [Trigger][SetLevel1] :  Set the level of the specified trigger for a specific channel

            Arguments :
                Channel : C1 | C2 | C3 | C4 | EX | EX5 | LINE : You can pass a member of the ENUM TriggerSources, or it's string. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
                Value : The value in V where to place the trigger

            Returns :
                self.GetAllErrors() : List of errors
        """
        self.__instr__.write(f"{Channel.__channel__}:TRLV {Value}")
        return self.__baseclass__.GetAllErrors()

    def SetLevel2(self, Channel, Value: float):
        """
        PySDS [Trigger][SetLevel2] :  Set the level of the specified trigger for a specific channel

        WARNING : This function is not available on SPO devices

            Arguments :
                Channel : C1 | C2 | C3 | C4 | EX | EX5 | LINE : You can pass a member of the ENUM TriggerSources, or it's string. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
                Value : The value in V where to place the trigger

            Returns :
                self.GetAllErrors() : List of errors
        """
        self.__instr__.write(f"{Channel.__channel__}:TRLV2 {Value}")
        return self.__baseclass__.GetAllErrors()

    #
    #   MODE
    #

    def SetMode(self, Mode):
        """
        PySDS [Trigger][SetMode] :  Configure the mode of operation of the trigger

            Arguments :
                Mode : AUTO | NORM | SINGLE | STOP : Restrained to theses values by an enum.

            Returns :
                Float : The number of ms of delay
        """
        if Mode not in ["AUTO", "NORM", "SINGLE", "STOP", "STOP"]:
            return [1, -1]  # Emulate the standard return type

        self.__instr__.write(f"TRMD {Mode}")
        return self.__baseclass__.GetAllErrors()

    def GetMode(self):
        """
        PySDS [Trigger][GetMode] :  Read the mode of operation of the trigger

            Arguments :
                None

            Returns :
                String : The mode
        """
        return self.__instr__.query("TRMD?").strip().split(" ")[-1]

    #
    #   SELECT
    #

    def SetSelect(self, *args):
        """
        PySDS [Trigger][SetSelect] :  Configure the trigger for very advanced usages.

        WARNING :   Due to the very advanced usage of this function, and the poor traduction / updates of the documentation, I'm currently unable to provide checking.
                    Thus, the function will only pass settings as given, without even trying to make a compatibility check.

            Arguments :
                None

            Returns :
                self.GetAllErrors() : List of errors
        """
        cmd = ""
        for arg in args:
            cmd += arg + ","

        self.__instr__.write(f"TRSE {cmd}")
        return self.__baseclass__.GetAllErrors()

    def GetSelect(self):
        """
        PySDS [Trigger][GetSelect] :    Read the trigger select configuration

        WARNING : Due to the complexity of this function, and the lack of proper traduction / explanations, this function only return a string.

            Arguments :
                None

            Returns :
                String :Command output
        """
        return self.__instr__.query("TRSE?").strip().split(" ")[-1]

    #
    #   SLOPE
    #

    def SetSlope(self, Channel, Slope):
        """
        PySDS [Trigger][SetSlope] :  Configure the 'orientation' of the edge used to trigger.

            Arguments :
                Channel : The channel used for trigger. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
                Slope : NEG | POS | WINDOW : The edge used to trigger

            Returns :
                self.GetAllErrors() : List of errors TRSL
        """
        if Channel not in ["C1", "C2", "C3", "C4", "EX", "EX5", "LINE"]:
            return [1, -1]  # Emulate the standard return type
        if Slope not in ["POS", "NEG", "WINDOWS"]:
            return [1, -2]  # Emulate the standard return type

        self.__instr__.write(f"{Channel.__channel__}:TRSL {Slope}")
        return self.__baseclass__.GetAllErrors()

    def GetSlope(self, Channel):
        """
        PySDS [Trigger][GetSlope] :  Return the configured slope for the trigger

            Arguments :
                Channel : The channel used for trigger. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)

            Returns :
                String : The slope used
        """
        if Channel not in ["C1", "C2", "C3", "C4", "EX", "EX5", "LINE"]:
            return [1, -1]  # Emulate the standard return type

        return self.__instr__.query(f"{Channel.__channel__}:TRSL?").strip().split(" ")[-1][:3]

    #
    #   WINDOW
    #

    def SetWindow(self, Value: float):
        """
        PySDS [Trigger][SetWindow] :  Set the height of the Window used for trigger

            Arguments :
                Value (float) : The value in volt

            Returns :
                self.GetAllErrors() : List of errors
        """
        self.__instr__.write(f"TRWI {Value}V")
        return self.__baseclass__.GetAllErrors()

    def GetWindow(self):
        """
        PySDS [Trigger][GetWindow] :  Get the height of the trigger window

            Arguments :
                None

            Returns :
                Value in volt (float)
        """
        return float(self.__instr__.query("TRWI?").strip().split(" ")[-1][:-1])

    #
    #   PATTERN
    #

    def SetPattern(self, Sources: list, Status: list, Pattern):
        """
        PySDS [Trigger][SetPattern] :  Configure a triggering pattern (Enable multi channel triggering)

            Arguments :
                Source : List of the sources used for the operation. Can only be C1 | C2 | C3 | C4
                Status : List of the status for each source : X | L | H (X = don't care)
                Pattern : AND | OR | NAND | NOR

            Returns :
                self.GetAllErrors() : List of errors
        """
        for Source in Sources:
            if Source not in ["C1", "C2", "C3", "C4"]:
                return [1, -1]  # Emulate the standard return type

        for State in Status:
            if State not in ["X", "L", "H"]:
                return [1, -2]  # Emulate the standard return type

        if Pattern not in ["AND", "OR", "NAND", "NOR"]:
            return [1, -3]  # Emulate the standard return type

        if len(Sources) != len(Status):
            return [1, -3]  # Emulate the standard return type

        if len(Sources) < 1:
            return [1, -3]  # Emulate the standard return type

        cmd = ""
        for index in range(len(Sources)):
            cmd += Sources[index] + "," + Status[index] + ","

        self.__instr__.write(f"TRPA {cmd}STATE,{Pattern}")
        return self.__baseclass__.GetAllErrors()

    def GetPattern(self):
        """
        PySDS [Trigger][GetPattern] : Read the used pattern trigger

            Arguments :
                None

            Returns :
                List of Channel, Conditions and Pattern
        """

        Ret = self.__instr__.query("TRPA?").strip().split(" ")[-1].split(",")

        Pattern = Ret[-1]
        Sources = []
        Conditions = []

        for index in range(0, 2 * int((len(Ret) - 2) / 2), 2):
            if Ret[index + 1] != "X":
                Sources.append(Ret[index])
                Conditions.append(Ret[index + 1])

        return Sources, Conditions, Pattern
