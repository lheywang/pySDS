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
    pySDS [Trigger][SiglentUART] : Class herited from SiglentBase.
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
