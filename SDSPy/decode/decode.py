# ============================================================================================================
# Decode.py
# lheywang on 21/12/2024
#
# Base file for the decode class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from ..channel import SiglentChannel
from ..digital import SiglentDChannel


class SiglentDecode(SiglentBase):
    """
    pySDS [Decode][SiglentDecode] : Class herited from SiglentBase.
                                    Store all command related the control of digital bus decoding
        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (12):

    """

    def EnableDecode(self):
        """
        pySDS [Decode][EnableDecode] : Enable the decode option on the scope

            Arguments :
                None

            Returns :
                True | False : The decode has been enabled or not
        """
        ret = self.__instr__.query("DCST ON").strip().split(" ")[-1]
        if ret == "ON":
            return True
        return False

    def DisableDecode(self):
        """
        pySDS [Decode][DisableDecode] : Disable the decode option on the scope

            Arguments :
                None

            Returns :
                True | False : The decode has been disabled, or not
        """
        ret = self.__instr__.query("DCST OFF").strip().split(" ")[-1]
        if ret == "OFF":
            return True
        return False

    def ConfigureDecode(
        self, Bus: int, Format="HEX", List="OFF", Link="", Scroll=0, Lines=0
    ):
        """
        pySDS [Decode][ConfigureDecode] : Configure the decode engine

            Arguments :
                Bus : 1 | 2 (Bus number)
                Format : BIN | DEC | HEX (Mode of print on screen) Default to HEX
                List : OFF | D1 | D2 Default to OFF
                Link : TR_TO_DC | DC_TO_TR
                Scroll : Integer
                Lines : Integer

            Returns :
                GetAllErrors() : List of errors
                or
                [n, Error codes] if errors occured within the function

            Errors codes :
                -1 :    Invalid Lines number
                -2 :    Invalid scroll number (must be > 0 and < Lines)
                -3 :    Invalid Link mode
                -4 :    Invalid List mode
                -5 :    Invalid format
                -6 :    Invalid Bus
        """
        # cmdeters check
        if Lines < 0 or Lines > 7:
            return [1, -1]
        if Scroll < 0 or Scroll > Lines:
            return [1, -2]
        if Link not in ["TR_TO_DC", "DC_TO_TR", ""]:
            return [1, -3]
        if List not in ["OFF", "D1", "D2"]:
            return [1, -4]
        if Format not in ["HEX", "DEC", "BIN"]:
            return [1, -5]
        if Bus < 1 or Bus > 2:
            return [1, -6]

        # Create the command string
        cmd = f"BUS,B{Bus},LIST,{List},FOMT,{Format}"
        if Link != "":
            cmd += f",LINK,{Link}"
        if Scroll != 0:
            cmd += f",LSSC,{List}"
        if Lines != 0:
            cmd += f",LSNM,{Lines}"

        self.__instr__.query(f"DCPA {cmd}")
        return self.__baseclass__.GetAllErrors()

    def ConfigureI2CDecode(
        self,
        Bus: int,
        SCL,
        SDA,
        SCLT: float = 1.65,
        SDAT: float = 1.65,
        Display="ON",
        RW="ON",
    ):
        """
        pySDS [Decode][ConfigureI2CDecode] : Configure the I2C decoding

        WARNING : If digital channel is provided, trigger level will be ignored

            Arguments :
                Bus :       Bus number, as in integer
                SCL :       SCL input. May be SiglentChannel or SiglentDigital class
                SDA :       SCL input. May be SiglentChannel or SiglentDigital class
                SCLT :      Trigger Level for SCL (Default to 1.65)
                SDAT :      Trigger Level for SCL (Default to 1.65)
                Display :   ON | OFF Display the bus decoding result (Default to ON)
                RW :        ON | OFF Display the Read/Write bit inside of adress, or not (Default to ON)

            Returns :
                GetAllErrors() : List of errors
                or
                List or errors codes within the function

            Errors codes :
                -1 :    Wrong object passed on SCL
                -2 :    Wrong object passed on SDA
                -3 :    Invalid mode for Display
                -4 :    Invalid mode for RW
                -5 :    Invalid bus number
        """

        # parameters check
        if (type(SCL) is not type(SiglentChannel)) and (
            type(SCL) is not type(SiglentDChannel)
        ):
            return [1, -1]
        if (type(SDA) is not type(SiglentChannel)) and (
            type(SDA) is not type(SiglentDChannel)
        ):
            return [1, -2]
        if Display not in ["ON", "OFF"]:
            return [1, -3]
        if RW not in ["ON", "OFF"]:
            return [1, -4]
        if Bus < 1 or Bus > 2:
            return [1, -5]

        # Command execution
        cmd = f"B{Bus}:DCIC "

        cmd += f"SCL,{SCL.__channel__}"
        if type(SCL) == type(SiglentChannel):
            cmd += f",SCLT,{SCLT}"

        cmd += f",SDA,{SDA.__channel__}"
        if type(SDA) == type(SiglentChannel):
            cmd += f",SDAT,{SDAT}"

        cmd += f",DIS,{Display},RW,{RW}"

        self.__instr__.write(cmd)

        # Returns
        return self.__baseclass__.GetAllErrors()

    def ConfigureSPIDecode(
        self,
        Bus: int,
        CLK,
        MOSI,
        MISO,
        CS,
        CSMode="CS",
        Edge="RISING",
        Bit="MSB",
        Len=8,
        CLKT=1.65,
        MOSIT=1.65,
        MISOT=1.65,
        CST=1.65,
        CSTimeout=2,
        Display="ON",
    ):
        """
        pySDS [Decode][ConfigureSPIDecode] : Configure the decoding of the SPI Bus

        WARNING : If a digital channel is provided, it's trigger value will be ignored

            Arguments  :
                Bus :       1 | 2 Bus used to decode
                CLK :       Channel for CLK. May be a channel or a digital channel
                MOSI :      Channel for MOSI. May be a channel or a digital channel
                MISO :      Channel for MISO. May be a channel or a digital channel
                CS :        Channel for CS. May be a channel or a digital channel
                CSMode :    CS | NCS | TIMEOUT Configure the CS operation mode                                          Defaults to CS
                Edge :      RISING | FALLING Configure the mode of SPI between mode 0, 2 : Falling or 1, 3 : Rising     Defaults to RISING
                Bit :       MSB | LSB Configure the bit order                                                           Defaults to MSB
                Len :       Configure the transfer length                                                               Defaults to 8 bit
                CLKT :      Configure the trigger level of the CLK.                                                     Defaults to 1.65.
                MOSIT :     Configure the trigger level of the MOSI.                                                    Defaults to 1.65.
                MISOT :     Configure the trigger level of the MISO.                                                    Defaults to 1.65.
                CST :       Configure the trigger level of the CS.                                                      Defaults to 1.65.
                CSTimeout : Timeout value for the CS when in timeout mode                                               Defaults to 2 (us)
                Display :   ON | OFF Display the result on the screen                                                   Defaults to ON

            Returns :
                GetAllErrors() : List of errors
                Or
                List of errors that occured within the function

            Errors codes :
                -1 :    Incorrect type passed for CLK. Waiting for a SiglentChannel or SiglentDChannel
                -2 :    Incorrect type passed for MOSI. Waiting for a SiglentChannel or SiglentDChannel
                -3 :    Incorrect type passed for MISO. Waiting for a SiglentChannel or SiglentDChannel
                -4 :    Incorrect type passed for CS. Waiting for a SiglentChannel or SiglentDChannel
                -5 :    Invalid CS Mode
                -6 :    Invalid Bus
                -7 :    Invalid Edge provided
                -8 :    Invalid bit provided
                -9 :    Len is out of bounds (4-32)
                -10 :   Invalid display mode
        """
        # parameters check
        if (type(CLK) is not type(SiglentChannel)) and (
            type(CLK) is not type(SiglentDChannel)
        ):
            return [1, -1]
        if (type(MOSI) is not type(SiglentChannel)) and (
            type(MOSI) is not type(SiglentDChannel)
        ):
            return [1, -2]
        if (type(MISO) is not type(SiglentChannel)) and (
            type(MISO) is not type(SiglentDChannel)
        ):
            return [1, -3]
        if (type(CS) is not type(SiglentChannel)) and (
            type(CS) is not type(SiglentDChannel)
        ):
            return [1, -4]
        if CSMode not in ["CS", "NCS", "TIMEOUT"]:
            return [1, -5]
        if Bus < 1 or Bus > 2:
            return [1, -6]
        if Edge not in ["RISING", "FALLING"]:
            return [1, -7]
        if Bit not in ["MSB", "LSB"]:
            return [1, -8]
        if Len < 4 or Len > 32:
            return [1, -9]
        if Display not in ["ON", "OFF"]:
            return [1, -10]

        # Creating command
        cmd = f"B{Bus}:DCSP ,MISO,{MISO.__channel__},MOSI,{MOSI.__channel__}"

        cmd += f"CLK,{CLK.__channel__}"
        if type(CLK) == type(SiglentChannel):
            cmd += f",CLKT,{CLKT}"
        cmd += f",MISO,{MISO.__channel__}"
        if type(MISO) == type(SiglentChannel):
            cmd += f",MISOT,{MISOT}"
        cmd += f",MOSI,{MOSI.__channel__}"
        if type(MOSI) == type(SiglentChannel):
            cmd += f",MOSIT,{MOSIT}"

        # Acting depending the chip select mode
        if CSMode == "CS":
            cmd += f",CS,{CS.__channel__}"
            if type(CST) == type(SiglentChannel):
                cmd += f",CST,{CST}"

        elif CSMode == "NCS":
            cmd += f",NCS,{CS.__channel__}"
            if type(CST) == type(SiglentChannel):
                cmd += f",NCST,{CST}"

        elif CSMode == "TIMEOUT":
            cmd += f",TIM,{CSTimeout}"

        cmd += f",EDGE,{Edge},DLEN,{Len},BIT,{Bit},DIS,{Display}"

        # Executing the command
        self.__instr__.write(cmd)

        # Returns errors
        return self.__baseclass__.GetAllErrors()

    def ConfigureUARTDecode():
        pass

    def ConfigureCANDecode():
        pass

    def ConfigureLINDecode():
        pass
