# ============================================================================================================
# SPI.py
# lheywang on 02/01/2025
#
# Advanced file for the trigger class, specialized on SPI bus
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel
from digital import SiglentDChannel


class SiglentSPI(SiglentBase):
    """
    pySDS [Trigger][SiglentSPI] :   Class herited from SiglentBase.
                                    Store all command related the control of the triggering system for the SPI bus

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (15):
                SetTriggerOnCLK :                   Set trigger on CLK Pin
                SetTriggerClockEdge :               Set trigger edge (act also on bus decoding)
                SetTriggerClockTimeout :            Set trigger timeout (act also on bus decoding)
                SetTriggerOnMOSI :                  Set trigger on MOSI Pin
                SetTriggerOnMISO :                  Set trigger on MISO Pin
                SetTriggerCSType :                  Set trigger Type (act also on bus decoding)
                SetTriggerOnCS :                    Set trigger on CS Pin
                SetTriggerOnNCS :                   Set trigger on NCS Pin
                ConfigureTriggerSource :            Set trigger Data Source
                ConfigureTriggerDataSequence :      Set trigger data Sequence
                ConfigureTriggerDataLen :           Set trigger Data Len
                SetTriggerBitOrder :                Set trigger bit order (act also on bus decoding)
    """

    def SetTriggerOnCLK(self, Channel, Threshold=1.65):
        """
        pySDS [SPI][SetTriggerOnCLK] : Configure the trigger on the SCLK pin.

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the SCLK pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRSPI:CLK {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerClockEdge(self, Edge: str):
        """
        pySDS [SPI][SetTriggerClockEdge] : Configure the edge of the clock the data is latched on

            Arguments :
                Edge : RISING | FALLING. The edge used.

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid edge
        """
        if Edge not in ["RISING", "FALLING"]:
            return [1, -1]

        self.__instr__.write(f"TRSPI:CLK:EDGE {Edge}")
        return self.__baseclass__.GetAllErrors()

    def SetTriggerClockTimeout(self, Timeout: str):
        """
        pySDS [SPI][SetTriggerClockTimeout] : Set the timeout value (related to clock) when the CS is timeout.

            Arguments :
                Timeout : from 100ns to 500ms (no check done)

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"TRSPI:CLK:TIM {Timeout}")
        return self.__baseclass__.GetAllErrors()

    def SetTriggerOnMOSI(self, Channel, Threshold=1.65):
        """
        pySDS [SPI][SetTriggerOnMOSI] : Configure the trigger on the MOSI pin.

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the MOSI pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRSPI:MOSI {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerOnMISO(self, Channel, Threshold=1.65):
        """
        pySDS [SPI][SetTriggerOnMISO] : Configure the trigger on the MOSI pin

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the MISO pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRSPI:MISO {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerCSType(self, Type: str):
        """
        pySDS [SPI][SetTriggerCSType] : Set the CS type on the SPI bus

            Arguments :
                Type : CS | NCS | TIMEOUT

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid type
        """
        if Type not in ["CS", "NCS", "TIMEOUT"]:
            return [1, -1]

        self.__instr__.write(f"TRSPI:CSTP {Type}")

    def SetTriggerOnCS(self, Channel, Threshold=1.65):
        """
        pySDS [SPI][SetTriggerOnMISO] : Configure the trigger on the CS pin

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the CS pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRSPI:CS {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerOnNCS(self, Channel, Threshold=1.65):
        """
        pySDS [SPI][SetTriggerOnMISO] : Configure the trigger on the NCS pin

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the NCS pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRSPI:NCS {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerSource(self, Source: str):
        """
        pySDS [SPI][ConfigureTriggerSource] : Configure the trigger source for the SPI

            Arguments :
                Source : MOSI | MISO

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid source
        """
        if Source not in ["MOSI", "MISO"]:
            return [1, -1]

        self.__instr__.write(f"TRSPI:TRTY {Source}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerDataSequence(self, Sequence: list):
        """
        pySDS [SPI][ConfigureTriggerDataSequence] : Configure a matching bit sequence to trigger

            Arguments :
                Sequence : List of char / string : 0 | 1 | X to trigger. Len must match the datalen (not checked)

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid sequence (len not checked)
        """
        cmd = f"TRSPI:DATA "
        for char in Sequence:
            if char not in ["0", "1", "X"]:
                return [1, -1]
            cmd += f"{char},"
        cmd = cmd[:-1]  # removing last ","

        self.__instr__.write(cmd)
        return self.GetAllErrors()

    def ConfigureTriggerDataLen(self, Len: int):
        """
        pySDS [SPI][ConfigureTriggerDataSequence] : Configure a matching data lenght to trigger

            Arguments :
                Len : 4-96

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Len
        """
        if Len < 4 or Len > 96:
            return [1, -1]

        self.__instr__.write(f"TRSPI:DLEN {Len}")
        return self.__baseclass__.GetAllErrors()

    def SetTriggerBitOrder(self, Order: str):
        """
        pySDS [SPI][SetTriggerBitOrder] : Set the bit order on the SPI Bus

            Arguments :
                Order : MSB | LSB

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid order
        """
        if Order not in ["LSB", "MSB"]:
            return [1, -1]

        self.__instr__.write(f"TRSPI:BIT {Order}")
        return self.__baseclass__.GetAllErrors()
