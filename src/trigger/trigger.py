# ============================================================================================================
# Trigger.py
# lheywang on 19/12/2024
#
# Base file for the trigger class
#
# ============================================================================================================

from enum import Enum

# Declaring our enums to prevent the user from sending unwanted values
TriggerSources = Enum(
    "Sources",
    [
        ("C1", "C1"),
        ("C2", "C2"),
        ("C3", "C3"),
        ("C4", "C4"),
        ("EX", "EX"),
        ("EX5", "EX5"),
        ("LINE", "LINE"),
    ],
)

TriggerModes = Enum(
    "Modes", [("AC", "AC"), ("DC", "DC"), ("HFREJ", "HFREJ"), ("LFREJ", "LFREJ")]
)

TriggerOperation = Enum(
    "Triggering Mode",
    [("AUTO", "AUTO"), ("NORM", "NORM"), ("SINGLE", "SINGLE"), ("STOP", "STOP")],
)

TriggerEdges = Enum("Edges", [("POS", "POS"), ("NEG", "NEG"), ("WINDOW", "WINDOWS")])

TriggerStatus = Enum("Status", [("X", "X"), ("L", "L"), ("H", "H")])

TriggerPattern = Enum(
    "Pattern", [("AND", "AND"), ("OR", "OR"), ("NAND", "NAND"), ("NOR", "NOR")]
)


class SiglentTrigger:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass

    #
    #   COUPLING
    #

    def SetCoupling(self, Channel: TriggerSources, Mode: TriggerModes):
        """
        PySDS [Trigger][SetCoupling] :  Configure the source and coupling of the trigger

        WARNING : The command to know the state of the trigger hasn't been developped since it suppose we know the channel used...

            Arguments :
                Channel : C1 | C2 | C3 | C4 | EX | EX5 | LINE : You can pass a member of the ENUM TriggerSources, or it's string. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
                Mode : AC | DC | HFREF | LFREJ : You can pass a member of the ENUM TriggerModes or it's name direcly

            Returns :
                self.GetAllErrors() : List of errors
        """
        if Channel not in TriggerSources:
            print(
                "     [ PySDS ] [ Trigger ] [ SetCoupling ] : Incorrect channel descriptor"
            )
            return [1, -1]  # Emulate the standard return type

        if Mode not in TriggerModes:
            print(
                "     [ PySDS ] [ Trigger ] [ SetCoupling ] : Incorrect mode descriptor"
            )
            return [1, -2]  # Emulate the standard return type

        self.__instr__.write(f"{Channel}:TRCP {Mode}")
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

    def SetLevel1(self, Channel: TriggerSources, Value: float):
        """
        PySDS [Trigger][SetLevel1] :  Set the level of the specified trigger for a specific channel

            Arguments :
                Channel : C1 | C2 | C3 | C4 | EX | EX5 | LINE : You can pass a member of the ENUM TriggerSources, or it's string. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
                Value : The value in V where to place the trigger

            Returns :
                self.GetAllErrors() : List of errors
        """
        self.__instr__.write(f"{Channel}:TRLV {Value}")
        return self.__baseclass__.GetAllErrors()

    def SetLevel2(self, Channel: TriggerSources, Value: float):
        """
        PySDS [Trigger][SetLevel2] :  Set the level of the specified trigger for a specific channel

        WARNING : This function is not available on SPO devices

            Arguments :
                Channel : C1 | C2 | C3 | C4 | EX | EX5 | LINE : You can pass a member of the ENUM TriggerSources, or it's string. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
                Value : The value in V where to place the trigger

            Returns :
                self.GetAllErrors() : List of errors
        """
        self.__instr__.write(f"{Channel}:TRLV2 {Value}")
        return self.__baseclass__.GetAllErrors()

    #
    #   MODE
    #

    def SetMode(self, Mode: TriggerOperation):
        """
        PySDS [Trigger][SetMode] :  Configure the mode of operation of the trigger

            Arguments :
                Mode : AUTO | NORM | SINGLE | STOP : Restrained to theses values by an enum.

            Returns :
                Float : The number of ms of delay
        """
        if Mode not in TriggerOperation:
            print("     [ PySDS ] [ Trigger ] [ SetMode ] : Incorrect mode descriptor")
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

    def SetSlope(self, Channel: TriggerSources, Slope: TriggerEdges):
        """
        PySDS [Trigger][SetSlope] :  Configure the 'orientation' of the edge used to trigger.

            Arguments :
                Channel : The channel used for trigger. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
                Slope : NEG | POS | WINDOW : The edge used to trigger

            Returns :
                self.GetAllErrors() : List of errors TRSL
        """
        if Channel not in TriggerSources:
            print(
                "     [ PySDS ] [ Trigger ] [ SetSlope ] : Incorrect source descriptor"
            )
            return [1, -1]  # Emulate the standard return type
        if Slope not in TriggerEdges:
            print(
                "     [ PySDS ] [ Trigger ] [ SetSlope ] : Incorrect slope descriptor"
            )
            return [1, -2]  # Emulate the standard return type

        self.__instr__.write(f"{Channel}:TRSL {Slope}")
        return self.__baseclass__.GetAllErrors()

    def GetSlope(self, Channel: TriggerSources):
        """
        PySDS [Trigger][GetSlope] :  Return the configured slope for the trigger

            Arguments :
                Channel : The channel used for trigger. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)

            Returns :
                String : The slope used
        """
        if Channel not in TriggerSources:
            print(
                "     [ PySDS ] [ Trigger ] [ SetSlope ] : Incorrect source descriptor"
            )
            return [1, -1]  # Emulate the standard return type

        return self.__instr__.query(f"{Channel}:TRSL?").strip().split(" ")[-1][:3]

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

    def SetPattern(self, Sources: list, Status: list, Pattern: TriggerPattern):
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
                print(
                    "     [ PySDS ] [ Trigger ] [ SetPattern ] : At least one incorrect channel was found"
                )
                return [1, -1]  # Emulate the standard return type

        for State in Status:
            if State not in TriggerStatus:
                print(
                    "     [ PySDS ] [ Trigger ] [ SetPattern ] : At least one incorrect status was found"
                )
                return [1, -2]  # Emulate the standard return type

        if Pattern not in TriggerPattern:
            print(
                "     [ PySDS ] [ Trigger ] [ SetPattern ] : At least one incorrect status was found"
            )
            return [1, -3]  # Emulate the standard return type

        if len(Sources) != len(Status):
            print(
                "     [ PySDS ] [ Trigger ] [ SetPattern ] : The list of Sources and State does not match in lengh"
            )
            return [1, -3]  # Emulate the standard return type

        if len(Sources) < 1:
            print(
                "     [ PySDS ] [ Trigger ] [ SetPattern ] : Not enough settings passed"
            )
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
