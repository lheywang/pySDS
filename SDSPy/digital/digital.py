# ============================================================================================================
# Digital.py
# lheywang on 21/12/2024
#
# Base file for the digital class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from .digitalchannel import SiglentDChannel


class SiglentDigital(SiglentBase):
    """
    pySDS [Digital][SiglentDigital] :   Class herited from SiglentBase.
                                        Store all command related the control of digital channels (scopes with MSO option only)

        WARNING :   This section of code is extremely undocumented, and the rare parts that are documentation aren't comprehesible.
                    Take all of this code with salt, since bugs can exists here due to an error of my person, or an error of the doc, or both
                    If something went bugging here, you can report it !

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (5):
                EnableDigitalChannel :          Enable a channel
                DisableDigitalChannel :         Disable a channel
                SetDigitalChannelThreshold :    Configure threshold for a group of channels
                EnableDigital :                 Enable global digital engine
                DisableDigital :                Disable global digital engine
    """

    def EnableDigitalChannel(self, Channel: SiglentDChannel):
        """
        pySDS [Digital][EnableDigitalChannel] : Enable a digital channel and display it on the screen

            Arguments :
                Channel : SiglentDChannel to be enabled and shown

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{Channel.__channel__}:DGCH ON")
        return self.__baseclass__.GetAllErrors()

    def DisableDigitalChannel(self, Channel: SiglentDChannel):
        """
        pySDS [Digital][DisableDigitalChannel] : Disable a digital channel and display it on the screen

            Arguments :
                Channel : SiglentDChannel to be disabled and hide

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"{Channel.__channel__}:DGCH OFF")
        return self.__baseclass__.GetAllErrors()

    def SetDigitalChannelThreshold(self, Group: int, Threshold, Value=0):
        """
        pySDS [Digital][SetDigitalChannelThreshold] : Configure the threshold for a type of logic signals.

        WARNING : This setting is applied for a group of 8 channels. There is only two groups.

            Arguments :
                Group : 1 | 2 Group where the setting is applied
                Threshold : TTL | CMOS | CMOS3.3 | CMOS2.5 | CUSTOM
                Value : Only for CUSTOM, the value in V between -5 and 5

            Returns :
                self.GetAllErrors() : List of errors
                or
                Errors codes

            Errors codes :
                -1 : Invalid group
                -2 : Invalid Threshold type
                -3 : Invalid value
        """
        if Group not in [1, 2]:
            return [1, -1]
        if Threshold not in ["TTL", "CMOS", "CMOS3.3", "CMOS2.5", "CUSTOM"]:
            return [1, -2]
        if Value < -5 or Value > 5:
            return [1, -3]

        cmd = f"C{Group}:DGTH {Threshold}"
        if Threshold == "CUSTOM":
            cmd += f",{Value}V"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def EnableDigital(self):
        """
        pySDS [Digital][EnableDigital] : Enable the digital section on the scope

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("DI:SW ON")
        return self.__baseclass__.GetAllErrors()

    def DisableDigital(self):
        """
        pySDS [Digital][DisableDigital] : Disable the digital section on the scope

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.query("DI:SW OFF")
        return self.__baseclass__.GetAllErrors()
