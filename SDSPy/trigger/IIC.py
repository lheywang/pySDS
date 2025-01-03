# ============================================================================================================
# IIC.py
# lheywang on 02/01/2025
#
# Advanced file for the trigger class, specialized on IIC bus
#
# ============================================================================================================
from ..BaseOptionnalClass import SiglentBase
from ..channel import SiglentChannel
from ..digital import SiglentDChannel


class SiglentIIC(SiglentBase):
    """
    pySDS [Trigger][SiglentIIC] :   Class herited from SiglentBase.
                                    Store all command related the control of the triggering system for the I2C bus

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (10):
                SetTriggerOnSCL :               Set the trigger on the SCL Bus
                SetTriggerOnSDA :               Set the trigger on the SDA Bus
                SetTriggerOnCondition :         Set the trigger on advanced conditions
                ConfigureTriggerAddress :       Set the trigger address condition
                ConfigureTriggerData1 :         Set the trigger data 1 condition
                ConfigureTriggerData2 :         Set the trigger data 2 condition
                ConfigureTriggerQual :          Set the trigger eeprom qualifier condition
                ConfigureTriggerRW :            Set the read / write condition
                ConfigureTriggerAddressLen :    Set the address len condition
                ConfigureTriggerDataLen :       Set the data len condition
    """

    def SetTriggerOnSCL(self, Channel, Threshold=1.65):
        """
        pySDS [IIC][SetTriggerOnSCL] : Configure the trigger on the SCL bus.

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the SCL pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRIIC:SCL {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerOnSDA(self, Channel, Threshold=1.65):
        """
        pySDS [IIC][SetTriggerOnSDA] : Configure the trigger on the SDA bus.

            Arguments :
                Channel :       SiglentChannel or SiglentDCHannel related to the SDA pin
                Threshold :     For analog channel only, the used voltage. Default to 1.65

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Channel
        """
        if type(Channel) is not SiglentChannel and type(Channel) is not SiglentDChannel:
            return [1, -1]

        cmd = f"TRIIC:SDA {Channel.__channel__}"

        if type(Channel) == SiglentChannel:
            cmd += f",{Threshold}"

        self.__instr__.write(cmd)
        return self.__baseclass__.GetAllErrors()

    def SetTriggerOnCondition(self, Condition: str):
        """
        pySDS [IIC][SetTriggerOnCondition] : Set the trigger on a bus transfer condition

        WARNING : Once the condition is selected, further configuration may be needed.

            Arguments :
                Condition : The selected condition

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid condition

            Possibles conditions :
                START : Start condition.
                STOP : Stop condition.
                RESTART : Another start condition occurs before a stop condition.
                NOACK : Missing acknowledge.
                EEPROM : EEPROM frame containing (Start:Controlbyte:R:Ack:Data).
                7ADDA : 7-bit address frame containing (Start:Address7:R/W:Ack:Data:Data2).
                10ADDA : 10-bit address frame containing (Start:Address10:R/W:Ack:Data:Data2).
                DALENTH : specifie a search based on address lengthand data length.
        """
        if Condition not in [
            "START",
            "STOP",
            "RESTART",
            "NOACK",
            "EEPROM",
            "7ADDA",
            "10ADDA",
            "DALENTH",
        ]:
            return [1, -1]

        self.__instr__.write(f"TRIIC:CON {Condition}")

    def ConfigureTriggerAddress(self, Address: int):
        """
        pySDS [IIC][ConfigureTriggerAddress] : Set the trigger on a specific address on the bus (7ADDA or 10ADDA only)

        WARNING : A condition must be configured to access to this function

            Arguments :
                Address : The device address, 0-128 or 0-1024 (7 or 10 bit address). Address is casted to integer prior device write.

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"TRIIC:ADDR {int(Address)}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerData1(self, Data: int):
        """
        pySDS [IIC][ConfigureTriggerData1] : Set the first byte of data on the bus to be filtered (7ADDA or 10ADDA only)

        WARNING : A condition must be configured to access to this function

            Arguments :
                Data : The data, 0-256. Data is casted to integer prior device write.

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"TRIIC:DATA {Data}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerData2(self, Data: str):
        """
        pySDS [IIC][ConfigureTriggerData2] : Set the second byte of data on the bus to be filtered (7ADDA or 10ADDA only)

        WARNING : A condition must be configured to access to this function

            Arguments :
                Data : The data, 0-256. Data is casted to integer prior device write.

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"TRIIC:DAT2 {Data}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerQual(self, Qual: str):
        """
        pySDS [IIC][ConfigureTriggerQual] : Configure the qualifier on the bus (EEPROM mode only)

        WARNING : A condition  must be configured to access to this function

            Arguments :
                Qaulifier : EQUAL | MORE | LESS

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid qualifier
        """

        if Qual not in ["MORE", "LESS", "EQUAL"]:
            return [1, -1]

        self.__instr__.write(f"TRIIC:QUAL {Qual}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerRW(self, RW: str):
        """
        pySDS [IIC][ConfigureTriggerRW]: Configure the trigger to detect read or write operations

        WARNING : A condition must be configured to access to this function

            Arguments :
                RW : READ | WRITE | DONT_CARE

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid RW
        """
        if RW not in ["READ", "WRITE", "DONT_CARE"]:
            return [1, -1]

        self.__instr__.write(f"TRIIC:RW {RW}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerAddressLen(self, Addr: str):
        """
        pySDS [IIC][ConfigureTriggerAddressLen] : Configure the size of the address to be waited. (Data Len mode only)

        WARNING : A condition must be configured to access to this function

            Arguments :
                Addr : 7BIT | 10BIT

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Address len
        """
        if Addr not in ["7BIT", "10BIT"]:
            return [1, -1]

        self.__instr__.write(f"TRIIC:ALEN {Addr}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureTriggerDataLen(self, Len: int):
        """
        pySDS [IIC][ConfigureTriggerDataLen] : Configure the number of byte in the message to trigger. (Data Len mode only)

        WARNING : A condition must be configured to access to this function

            Arguments :
                Len : Integer, between 1 and 12

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid Len
        """
        if Len < 1 or Len > 12:
            return [1, -1]

        self.__instr__.write(f"TRIIC:DLEN {Len}")
        return self.__baseclass__.GetAllErrors()
