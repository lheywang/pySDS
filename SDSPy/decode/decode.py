# ============================================================================================================
# Decode.py
# lheywang on 21/12/2024
#
# Base file for the decode class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase


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
    
    def ConfigureDecode(self, Bus : int, Format = "HEX", List = "OFF", Link = "", Scroll = 0, Lines = 0):
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
        # Parameters check
        if Lines < 0 or Lines > 7:
            return [1, -1]
        if Scroll < 0 or Scroll > Lines :
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
        param = f"BUS,B{Bus},LIST,{List},FOMT,{Format}"
        if Link != "":
            param += f",LINK,{Link}"
        if Scroll != 0:
            param += f",LSSC,{List}"
        if Lines != 0:
            param += f",LSNM,{Lines}"

        self.__instr__.query(f"DCPA {param}")
        return self.__baseclass__.GetAllErrors()
    
    # def ConfigureI2CDecode(self, Bus : int)
    # To be done : Create a digital channel object that can be accepted here !