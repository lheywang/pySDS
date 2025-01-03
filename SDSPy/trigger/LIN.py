# ============================================================================================================
# LIN.py
# lheywang on 02/01/2025
#
# Advanced file for the trigger class, specialized on LIN bus
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel
from digital import SiglentDChannel


class SiglentLIN(SiglentBase):
    """
    pySDS [Trigger][SiglentLIN] :   Class herited from SiglentBase.
                                    Store all command related the control of the triggering system for the LIN bus

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (15):

    """

    def SetTriggerOnSRC(self, Channel, Threshold=1.65):
        """
        pySDS [LIN][SetTriggerOnSRC] : Configure the trigger on the LIN pin

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the LIN pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRLIN:SRC {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerOnCondition(self, Condition: str):
        """
        pySDS [LIN][SetTriggerOnCondition] : Configure the trigger on a condition on the CAN Bus

            Arguments :
                Condition : BREAK | DATA_ERROR | ID | ID_AND_DATA

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid condition

            Possibles conditions :
                BREAK— Break condition.
                ID— Specify a search based on ID.
                ID_AND_DATA—Specify a search based on ID and data.
                DATA_ERROR— Error frame.
        """
        if Condition not in ["BREAK", "DATA_ERROR", "ID", "ID_AND_DATA"]:
            return [1, -1]

        self.__instr__.write(f"TRLIN:CON {Condition}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerID(self, ID: int):
        """
        pySDS [LIN][ConfigureTriggerID] : Set the ID for ID and ID_AND_DATA mode of trigger

            Arguments :
                ID : Integer between 0-64

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid ID
        """
        if ID < 0 or ID > 64:
            return [1, -1]

        self.__instr__.write(f"TRLIN:ID {ID}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerData1(self, Value: int):
        """
        pySDS [LIN][ConfigureTriggerData1] : Configure the data (first byte) to be used to trigger for ID_AND_DATA mode.

            Arguments :
                Value: 0-255 value

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid value
        """
        if Value < 0 or Value > 255:
            return [1, -1]

        self.__instr__.write(f"TRLIN:DATA {Value}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerData2(self, Value: int):
        """
        pySDS [LIN][ConfigureTriggerData2] : Configure the data (second byte) to be used to trigger for ID_AND_DATA mode.

            Arguments :
                Value: 0-255 value

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid value
        """
        if Value < 0 or Value > 255:
            return [1, -1]

        self.__instr__.write(f"TRLIN:DAT2 {Value}")
        return self.__baseclass__.GetAllErrors()

    def SetTriggerBaud(self, Baud):
        """
        pySDS [LIN][SetTriggerBaud] : Set the baud rate of the UART comm

            Arguments :
                Baud : Value. (As a string for standard values, or as an integer for non standard)*

                * Sending a standard as integer will be seen as custom but will also works fine !

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Baud

            Standard baud values :
                600
                1200
                2400
                4800
                9600
                19200
        """
        if Baud < 300 or Baud > 20_000:
            return [1, -1]

        if Baud not in [600, 1200, 2400, 4800, 9600, 19200]:
            cmd = f"TRLIN:BAUD CUSTOM,{Baud}"
        else:
            cmd = f"TRLIN:BAUD {Baud}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()
