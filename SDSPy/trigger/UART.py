# ============================================================================================================
# UART.py
# lheywang on 02/01/2025
#
# Advanced file for the trigger class, specialized on Serial bus
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel
from digital import SiglentDChannel


class SiglentUART(SiglentBase):
    """
    pySDS [Trigger][SiglentUART] :  Class herited from SiglentBase.
                                    Store all command related the control of the triggering system for the UART bus

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (15):

    """

    def SetTriggerOnRX(self, Channel, Threshold=1.65):
        """
        pySDS [UART][SetTriggerOnRX] : Configure the trigger on the RX pin

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the RX pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRUART:RX {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerOnTX(self, Channel, Threshold=1.65):
        """
        pySDS [UART][SetTriggerOnTX] : Configure the trigger on the TX pin

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the TX pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRUART:TX {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerDataSource(self, Source: str):
        """
        pySDS [UART][SetTriggerDataSource] : Configure the used data source to trigger

            Arguments :
                Source : Data Source used RX | TX

            Returns :
                self.GetAllErrors
                or
                -1 : Invalid Source
        """
        if Source not in ["RX", "TX"]:
            return [1, -1]

        self.__instr__.write(f"TRUART:TRTY {Source}")
        return self.__baseclass__.GetAllErrors()

    def SetTriggerCondition(self, Condition):
        """
        pySDS [UART][SetTriggerCondition] : Set the trigger on a specific case

            Arguments :
                Condition : START | STOP | DATA | ERROR

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Condition
        """
        if Condition not in ["START", "STOP", "DATA", "ERROR"]:
            return [1, -1]

        self.__instr__.write(f"TRUART:CON {Condition}")
        return self.__baseclass__.GetAllErrors()

    def SetTriggerQualifier(self, Qualifier):
        """
        pYSDS [UART][SetTriggerQualifier] : Set the UART Qualifier condition

            Arguments :
                Qualifier : EQUAL | MORE | LESS

            Returns
                self.GetAllErrors()
                or
                -1 : Invalid qualifier
        """
        if Qualifier not in ["MORE", "LESS", "EQUAL"]:
            return [1, -1]

        self.__instr__.write(f"TRUART:QUAL {Qualifier}")

    def ConfigureTriggerData(self, Data):
        """
        pySDS [UART][ConfigureTriggerData] : Configure triggering data

            Arguments :
                Data : Data to be used

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid value
        """
        if int(Data) < 0 or int(Data) > 256:
            return [1, -1]

        self.__instr__.write(f"TRUART:DATA {Data}")
        return self.__baseclass__.GetAllErrors()

    def SetTriggerBaud(self, Baud):
        """
        pySDS [UART][SetTriggerBaud] : Set the baud rate of the UART comm

            Arguments :
                Baud : Value.

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Baud
        """
        if Baud < 300 or Baud > 5_000_000:
            return [1, -1]

        if Baud not in [600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]:
            cmd = f"TRUART:BAUD CUSTOM,{Baud}"
        else:
            cmd = f"TRUART:BAUD {Baud}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerDataLen(self, Len: int):
        """
        pySDS [UART][ConfigureTriggerDataLen] : Configure the number of bits to trigger

            Arguments :
                Len : 5 to 8

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Len
        """
        if Len < 5 or Len > 8:
            return [1, -1]

        self.__instr__.write(f"TRUART:DLEN {Len}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerParity(self, Parity: str):
        """
        pySDS [UART][ConfigureTriggerParity] : Configure the parity bit used

            Arguments :
                Parity : ODD | EVEN | NONE

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Parity
        """
        if Parity not in ["ODD", "EVEN", "NONE"]:
            return [1, -1]

        self.__instr__.write(f"TRUART:PAR {Parity}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerPolarity(self, Polarity: str):
        """
        pySDS [UART][ConfigureTriggerPolarity] : Configure the bus polarity

            Arguments :
                Polarity : LOW | HIGH

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Polarity
        """
        if Polarity not in ["LOW", "HIGH"]:
            return [1, -1]

        self.__instr__.write(f"TRUART:POL {Polarity}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerStop(self, Stop: float):
        """
        pySDS [UART][ConfigureTriggerStop] : Configure the number of stops bits used

            Arguments :
                Stop : 1 | 1.5 | 2

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid stop bit config
        """
        if Stop not in [1, 1.5, 2]:
            return [1, -1]

        self.__instr__.write(f"TRUART:STOP {Stop}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerBitOrder(self, Order: str):
        """
        pySDS [UART][ConfigureTriggerBitOrder] : Configure the bit order on the comm

            Arguments :
                Order : LSB | MSB

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Order
        """
        if Order not in ["LSB", "MSB"]:
            return [1, -1]

        self.__instr__.write(f"TRUART:BIT {Order}")
        return self.__baseclass__.GetAllErrors()
