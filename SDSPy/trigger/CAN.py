# ============================================================================================================
# CAN.py
# lheywang on 02/01/2025
#
# Advanced file for the trigger class, specialized on CAN bus
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel
from digital import SiglentDChannel


class SiglentCAN(SiglentBase):
    """
    pySDS [Trigger][SiglentCAN] :   Class herited from SiglentBase.
                                    Store all command related the control of the triggering system for the CAN bus

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (7):
                SetTriggerOnCANH :          Set trigger Pin.
                SetTriggerOnCondition :     Set trigger on a condition
                ConfigureTriggerID :        Set trigger ID
                ConfigureTriggerIDLen :     Set trigger ID Len
                ConfigureTriggerData1 :     Set trigger first byte
                ConfigureTriggerData2 :     Set trigger second byte
                SetTriggerBaud :            Set trigger baud

    """

    def SetTriggerOnCANH(self, Channel, Threshold=1.65):
        """
        pySDS [CAN][SetTriggerOnCANH] : Configure the trigger on the CANH pin

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the RCANH pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRCAN:CANH {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerOnCondition(self, Condition: str):
        """
        pySDS [CAN][SetTriggerOnCondition] : Configure the trigger on a condition on the CAN Bus

            Arguments :
                Condition : START | REMOTE | ID | ID_AND_DATA | ERROR

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid condition
        """
        if Condition not in ["START", "REMOTE", "ID", "ID_AND_DATA", "ERROR"]:
            return [1, -1]

        self.__instr__.write(f"TRCAN:CON {Condition}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerID(self, ID: int):
        """
        pySDS [CAN][ConfigureTriggerID] : Set the ID for ID and ID_AND_DATA mode of trigger

            Arguments :
                ID : Integer between 0-2048 (11 bits) or 0-536870912 (29 bits)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"TRCAN:ID {ID}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerIDLen(self, Len: str):
        """
        pySDS [CAN][ConfigureTriggerID] : Set the ID len for ID and ID_AND_DATA mode of trigger.

            Arguments :
                Len : 11BITS | 29BITS

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Len
        """
        if Len not in ["11BITS", "29BITS"]:
            return [1, -1]

        self.__instr__.write(f"TRCAN:IDL {Len}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerData1(self, Value: int):
        """
        pySDS [CAN][ConfigureTriggerData1] : Configure the data (first byte) to be used to trigger for ID_AND_DATA mode.

            Arguments :
                Value: 0-255 value

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid value
        """
        if Value < 0 or Value > 255:
            return [1, -1]

        self.__instr__.write(f"TRCAN:DATA {Value}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerData2(self, Value: int):
        """
        pySDS [CAN][ConfigureTriggerData2] : Configure the data (second byte) to be used to trigger for ID_AND_DATA mode.

            Arguments :
                Value: 0-255 value

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid value
        """
        if Value < 0 or Value > 255:
            return [1, -1]

        self.__instr__.write(f"TRCAN:DAT2 {Value}")
        return self.__baseclass__.GetAllErrors()

    def SetTriggerBaud(self, Baud):
        """
        pySDS [UART][SetTriggerBaud] : Set the baud rate of the UART comm

            Arguments :
                Baud : Value. (As a string for standard values, or as an integer for non standard)*

                * Sending a standard as integer will be seen as custom but will also works fine !

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Baud

            Standard baud values :
                5k
                10k
                20k
                50k
                100k
                125k
                250k
                500k
                800k
                1M
        """
        if Baud < 300 or Baud > 5_000_000:
            return [1, -1]

        if Baud not in [
            "5k",
            "10k",
            "20k",
            "59k",
            "100k",
            "125k",
            "250k",
            "500k",
            "800k",
            "1M",
        ]:
            cmd = f"TRUART:BAUD CUSTOM,{Baud}"
        else:
            cmd = f"TRUART:BAUD {Baud}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()
