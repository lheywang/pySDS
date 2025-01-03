# ============================================================================================================
# Timebase.py
# lheywang on 21/12/2024
#
# Base file for the timebase class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase


class SiglentTimebase(SiglentBase):
    """
    pySDS [Files][SiglentTimebase] :    Class herited from SiglentBase.
                                        Store all command related the control of timebase on the display

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (7):
    """

    def GetTimeDiv(self):
        """
        pySDS [Timebase][GetTimeDiv] : Return the time division used

            Arguments :
                None

            Returns :
                Time division used in seconds
        """
        return float(self.__instr__.query("TDIV?").strip().split(" ")[-1])

    def SetTimeDiv(self, Timebase: str):
        """
        pySDS [Timebase][SetTimeDiv] : Configure the timebase used

            Arguments :
                Timebase : Base to be used (from defined list right after)

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid timebase

            Possibles timebases :
                1NS 2NS 5NS
                10NS 20NS 50NS
                100NS 200NS 500NS
                1US 2US 5US
                10US 20US 50US
                100US 200US 500US
                1MS 2MS 5MS
                10MS 20MS 50MS
                100MS 200MS 500MS
                1S 2S 5S
                10S 20S 50S
                100S
        """
        if Timebase not in [
            "1NS",
            "2NS",
            "5NS",
            "10NS",
            "20NS",
            "50NS",
            "100NS",
            "200NS",
            "500NS",
            "1US",
            "2US",
            "5US",
            "10US",
            "20US",
            "50US",
            "100US",
            "200US",
            "500US",
            "1MS",
            "2MS",
            "5MS",
            "10MS",
            "20MS",
            "50MS",
            "100MS",
            "200MS",
            "500MS",
            "1S",
            "2S",
            "5S",
            "10S",
            "20S",
            "50S",
            "100S",
        ]:
            return [1, -1]
        self.__instr__.write(f"TDIV {Timebase}")
        return self.__baseclass__.GetAllErrors()

    def GetTriggerOffset(self):
        """
        pySDS [TimeBase][GetTriggerOffset] : Return the delay between trigger and center point

        - Pre-trigger acquisition — Data acquired before the trigger occurs. Negative trigger delays must be given in seconds.
        - Post-trigger acquisition — Data acquired after the trigger has occurred

            Arguments :
                None

            Returns :
                Time in seconds
        """
        return float(self.__instr__.query("TRDL?").strip().split(" ")[-1])

    def SetTriggerOffset(self, Offset):
        """
        pySDS [TimeBase][SetTriggerOffset] : Offset the delay between trigger and center point.

        - Pre-trigger acquisition — Data acquired before the trigger occurs. Negative trigger delays must be given in seconds.
        - Post-trigger acquisition — Data acquired after the trigger has occurred

            Arguments :
                Offset : Delay in seconds to offset

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"TRDL {Offset}S")
        return self.__baseclass__.GetAllErrors()

    def SetMagnifierZoom(self, Zoom):
        """
        pySDS [TimeBase][SetMagnifierZoom] : Configure the zoom on the screen.

            Arguments :
                Zoom : Two options (depending on the device !) :
                    - Time with units, from 1NS to current timebase (only checked globally, not for actual settings) ==> Pass an str type
                    - Factor, from 1 to 2 000 000 (Older !) ==> Pass a non str type

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid zoom

            Possibles timebases :
                1NS 2NS 5NS
                10NS 20NS 50NS
                100NS 200NS 500NS
                1US 2US 5US
                10US 20US 50US
                100US 200US 500US
                1MS 2MS 5MS
                10MS 20MS 50MS
                100MS 200MS 500MS
                1S 2S 5S
                10S 20S 50S
                100S
        """
        # Type 1, which is OLD !
        if type(Zoom) == str:
            if Zoom not in [
                "1NS",
                "2NS",
                "5NS",
                "10NS",
                "20NS",
                "50NS",
                "100NS",
                "200NS",
                "500NS",
                "1US",
                "2US",
                "5US",
                "10US",
                "20US",
                "50US",
                "100US",
                "200US",
                "500US",
                "1MS",
                "2MS",
                "5MS",
                "10MS",
                "20MS",
                "50MS",
                "100MS",
                "200MS",
                "500MS",
                "1S",
                "2S",
                "5S",
                "10S",
                "20S",
                "50S",
                "100S",
            ]:
                return [1, -1]
        else:
            if Zoom < 1 or Zoom > 2_000_000:
                return [1, -1]

        self.__instr__.write(f"HMAG {Zoom}")
        return self.__baseclass__.GetAllErrors()

    def SetMagnifierPosition(self, Position):
        """
        pySDS [TimeBase][SetMagnifierPosition] : Place the zoom position

            Arguments :
                Two options (depending on the device) :
                    - Time position, with units. ==> Pass an str type
                    - Div factor (older !) ==> Pass an non str type

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Position
        """
        if type(Position) == str:
            if Position not in [
                "1NS",
                "2NS",
                "5NS",
                "10NS",
                "20NS",
                "50NS",
                "100NS",
                "200NS",
                "500NS",
                "1US",
                "2US",
                "5US",
                "10US",
                "20US",
                "50US",
                "100US",
                "200US",
                "500US",
                "1MS",
                "2MS",
                "5MS",
                "10MS",
                "20MS",
                "50MS",
                "100MS",
                "200MS",
                "500MS",
                "1S",
                "2S",
                "5S",
                "10S",
                "20S",
                "50S",
                "100S",
            ]:
                return [1, -1]

        else:
            # No conditions specified, so what to do ?
            pass

        self.__instr__.write(f"HPOS {Position}")
        return self.__baseclass__.GetAllErrors()
