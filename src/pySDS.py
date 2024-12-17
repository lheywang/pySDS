# ============================================================================================================
# PySDS.py
# lheywang on 17/12/2024
#
# Base file for the whole package class
#
# ============================================================================================================

# Python libraries
import ipaddress
import tomllib

# Poetry managed lbraries
import pyvisa # type: ignore

# Others files
from channel import SDSChannel


class PySDS:
    """
    PySDS [class] : Parent class of the PySDS package. 
                    Handle actually all of basic SCPI commands, and call subclasses for some advanced functionnalities !

        Parents : 
            None
        
        Subclass :
            Channel
            
    """

    def __init__(self, IP: str):
        """
        PySDS [init] :  Initialize the class.
                        Use some configuration file to initialize properly the oscilloscope, and read it's actual state to make sure to fetch the real state
                        May take some time since a lot of network requests are done here !
        
            Arguments : 
                IP : A string IP address, version 4 of where the ressource shall be allocated
            
            Returns : 
                None
        """

        # First, validate the IP and try to open the ressource !
        try :
            self.__ip__ = ipaddress.ip_address(IP)
        except ValueError :
            print("     [ PySDS ] [ Init ] : Incorrect IP was passed to the constructor")
            return

        try :
            self.__rm__ = pyvisa.ResourceManager()
            self.__instr__ = self.__rm__.open_resource(f"TCPIP0::{IP}::inst0::INSTR")
        except :
            print("     [ PySDS ] [ Init ] : Unable to access to the device. Check if the IP is right, or if you can ping it !")
            return 

        # Then, request for the IDN command.
        # Typical return : Siglent Technologies,SDS824X HD,SDS08A0C802019,3.8.12.1.1.3.8
        IDN = self.__instr__.query('*IDN?')
        IDN = IDN.split(",")

        # Check if the brand is the right one, or this library isn't going to work !
        if IDN[0].find("Siglent") == -1:
            print("     [ PySDS ] [ Init ] : Found a non Siglent Device on this IP !") 
            return

        # Parse some different fields 
        self.model = IDN[1]
        self.SN = IDN[2]
        self.Firmware = IDN[3]

        # Load the right configuration file 
        # First, replace any space in the name with a "-" to ensure compatibility within different OS
        self.model = self.model.replace(" ", "-")

        # Load the right configuration file
        self.__ConfigFile__ = self.model + ".toml"

        self.__Config__ = None
        with open(f"config/{self.__ConfigFile__}", "rb") as f :
            self.__Config__ = tomllib.load(f)

        # Now, initialize some parameters from the configuration file
        for Channel in range(self.__Config__["Specs"]["Channel"]) :
            pass
            # Init here some standard channels
            # Make sure to load the settings direcly !

        # Then, load default settings by sending request to get the actual state of the device

        return
    
    def __repr__(self):
        """
        PySDS [repr] :  Basic print of the connected device.
                        Aimed to the developper, and thus expose more informations than the __str__ function !

            Arguments :
                None

            Returns :
                None
        """
        print(f"Device on {self.__ip__} :
                    Type : {self.model} ")
        return

    def __str__(self):
        """
        PySDS [repr] :  Basic print of the connected device.
                        Aimed to the user, and thus expose less informations than the __repr__ function !

            Arguments :
                None

            Returns :
                None
        """
        print(f"Device on {self.__ip__} :
            Type : {self.model} ")
        return
    


        
            

        


        
