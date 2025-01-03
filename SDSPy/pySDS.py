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
from datetime import datetime
from warnings import warn

# Poetry managed lbraries
import pyvisa  # type: ignore

# Others files
from acquisition import SiglentAcquisition
from channel import SiglentChannel
from communication import SiglentCommunication
from cursor import SiglentCursor
from decode import SiglentDecode
from deprecated_functions import ACAL, DATE, COUNTER
from digital import SiglentDigital
from display import SiglentScreen
from Files import SiglentFiles
from generics import SCPIGenerics
from history import SiglentHistory
from maths import SiglentMaths
from measure import SiglentMeasure
from passfail import SiglentPassFail
from references import SiglentReference
from timebase import SiglentTimebase
from trigger import SiglentTrigger
from waveform import SiglentWaveform


class PySDS:
    """
    PySDS [class] : Parent class of the PySDS package.
                    Handle actually all of basic SCPI commands, and call subclasses for some advanced functionnalities !

        Attributes :
            Private :
                __ip__ :            ip of the device. Used internally to check it's validity.
                __rm__ :            pyvisa ressource manager
                __instr__ :         Handle to the pyvisa object to interract with the device
                __ConfigFile__ :    Configuration file used for the scope.
                __Config__ :        Parsed configuration toml file
                __Generics__ :      SCPIGenerics class. Used for low level interraction with the device.

            Public :
                ** Standard variables **
                DeviceOpenned :     Get a non 0 value if the device was openned correctly. Otherwise, take 0
                model :             Device model, parsed from *IDN command
                SN :                Device SN, parsed from *IDN command
                Firmware :          Device firmware revision, parsed from *IDN command

                ** SCPI Variables **
                Channel :           A list of channel presents on the device. Each is it's own SiglentChannel class.
                Trigger :           A SiglentTrigger class



        Methods :
            Private :

            Public :

        Parents :
            None

        Subclass :
            None

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
        try:
            self.__ip__ = ipaddress.ip_address(IP)
        except ValueError:
            print(
                "     [ PySDS ] [ Init ] : Incorrect IP was passed to the constructor"
            )
            self.DeviceOpenned = 0
            return

        try:
            self.__rm__ = pyvisa.ResourceManager()
            self.__instr__ = self.__rm__.open_resource(f"TCPIP0::{IP}::inst0::INSTR")
        except:
            print(
                "     [ PySDS ] [ Init ] : Unable to access to the device. Check if the IP is right, or if you can ping it !"
            )
            self.DeviceOpenned = 0
            return

        # Then, request for the IDN command.
        # Typical return : Siglent Technologies,SDS824X HD,SDS08A0C802019,3.8.12.1.1.3.8
        IDN = self.__instr__.query("*IDN?")
        IDN = IDN.split(",")

        # Check if the brand is the right one, or this library isn't going to work !
        if IDN[0].find("Siglent") == -1:
            print("     [ PySDS ] [ Init ] : Found a non Siglent Device on this IP !")
            self.DeviceOpenned = 0
            return

        # Parse some different fields
        self.model = IDN[1]
        self.SN = IDN[2]
        self.Firmware = IDN[3]

        # Load the right configuration file
        # First, replace any space in the name with a "-" to ensure compatibility within different OS
        self.model = self.model.replace(" ", "-")

        # Load the right configuration file without the SDS in front
        self.__ConfigFile__ = self.model[3:] + ".toml"

        self.__Config__ = None
        with open(f"config/{self.__ConfigFile__}", "rb") as f:
            self.__Config__ = tomllib.load(f)

        # Create a generic class, for internal usage only
        self.__Generics__ = SCPIGenerics(self.__instr__, self)

        # Now, initialize some parameters from the configuration file
        self.Channel = []
        for index in range(self.__Config__["Specs"]["Channel"]):
            self.Channel.append(
                SiglentChannel(
                    self.__instr__, self, f"C{index}", self.__Config__["impedance"]
                )
            )

        # Then, initialize all of the subclass
        self.Acquistion = SiglentAcquisition(self.__instr__, self)
        self.Autotest = SiglentPassFail(self.__instr__, self)
        self.Communication = SiglentCommunication(self.__instr__, self)
        self.Cursor = SiglentCursor(self.__instr__, self)
        self.Decode = SiglentDecode(self.__instr__, self)
        self.Digital = SiglentDigital(self.__instr__, self)
        self.Display = SiglentScreen(self.__instr__, self)
        self.Files = SiglentFiles(self.__instr__, self)
        self.History = SiglentHistory(self.__instr__, self)
        self.Maths = SiglentMaths(self.__instr__, self)
        self.Measure = SiglentMeasure(self.__instr__, self)
        self.Reference = SiglentReference(self.__instr__, self)
        self.Trigger = SiglentTrigger(self.__instr__, self)
        self.Timebase = SiglentTimebase(self.__instr__, self)
        self.Waveform = SiglentWaveform(self.__instr__, self)

        # For some older device, load additionnal commands that are depecrated in the newest models / firmwares
        if "ACAL" in self.__Config__["Specs"]["LegacyFunctions"]:
            self.Calibration = ACAL(self.__instr__, self)

        if "DATE" in self.__Config__["Specs"]["LegacyFunctions"]:
            self.Date = DATE(self.__instr__, self)

        if "COUNTER" in self.__Config__["Specs"]["LegacyFunctions"]:
            self.Counter = COUNTER(self.__instr__, self)

        # Then, load default settings by sending request to get the actual state of the device

        # Check for support of depecrated commands !
        # ACAL (SDS2000X and SDS1000CFL)
        # AAUTS (Up to SDS1000X)
        # COUNTER (SDS1000 non SPO)
        # CSV SAVE (All but different formats...)
        # DATE (SDS2000X and SDS1000CFL)
        # FFTZOOM (Up to SDS1000X)
        # FILTER (SDS1000 non SPO)
        # FILT SET (SDS1000 non SPO)
        # PEAK DETECT (Up to SDS1000X)
        # PFCT (Up to SDS1000X)
        # PERS (Up to SDS1000X)
        # RECALL (Up to SDS1000X)
        # REFSET (Up to SDS1000X)
        # VPOS (Up to SDS1000X)

        self.DeviceOpenned = 1
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

        print(f"Device on {self.__ip__} : \nType : {self.model} ")
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

        print(f"Device on {self.__ip__} : \nType : {self.model} ")
        return

    #
    #   STATUS
    #

    def GetAllStatus(self):
        """
        PySDS [GetAllStatus] :  Return the status of the STB, ESR, INR, DDR, CMD, EXR and URR Registers.

            Arguments :
                None

            Returns :
                List of integers with the values in order
        """

        # Querry
        Ret = self.__instr__.query("ALST?")

        # Split comma. Format : ALST STB, Val, ESR..
        # Get only the usefull values
        Ret = Ret.strip().split(",")
        return [
            int(Ret[1]),
            int(Ret[3]),
            int(Ret[5]),
            int(Ret[7]),
            int(Ret[9]),
            int(Ret[11]),
            int(Ret[13]),
        ]

    #
    #   BUZZER
    #

    def EnableBuzzer(self):
        """
        PySDS [EnableBuzzer] :  Enable the device buzzer

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("BUZZ ON")
        return self.GetAllErrors()

    def DisableBuzzer(self):
        """
        PySDS [DisableBuzzer] : Disable the device buzzer

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("BUZZ OFF")
        return self.GetAllErrors()

    def GetBuzzerEnablingState(self):
        """
        PySDS [GetBuzzerEnablingState] :    Return the buzzer enabling state (ON or OFF)

        Arguments :
            None

        Returns :
            True | False
        """
        Ret = self.__instr__.query("BUZZ?").strip().split(" ")[-1]
        if Ret == "ON":
            return True
        return False

    #
    #   CALIBRATION
    #

    def Calibrate(self):
        """
        PySDS [Calibrate] : Calibrate the device.
                            This is actually the fast one, which does not do a full analog frontend calibration.

        WARNING :   Leaving probes and other elements connected may affect the result.
                    Make sure to calibrate the device in proper conditions !

        Arguments :
            None

        Returns :
            Integer : If 0, then calibration was sucessfull.
        """

        Ret = self.__instr__.query("*CAL?")
        return int(Ret.strip().split(" ")[-1])

    #
    #   AUTOSET
    #

    def Autoset(self):
        """
        pySDS [Autoset] : Launch an autoset procedure

        WARNING :   This should be avoided as possible, since the autoset isn't the most reliable thing in the world.
                    It's possible that the scope will show a detail of the waweform where there is some others things to be seen.
                    Use in a maximal number of case the manual settings to precisely control the predicted signal

            Arguments :
                None

            Returns :
                self.GetAllErrors() : List of errors that occured
        """
        self.__instr__.write("ASET")
        return self.GetAllErrors()

    #
    #   STANDARD SCPI COMMANDS
    #

    # =============================================================================================================================================
    """
    Up to this point, all functions shall be working on any device, even other than Siglent ones since they're part
    of the IEEE 488.1 specification.

    In any way, the class can't be constructed without a compatible device, that's why I didn't create a global SCPI engine...
    """
    # =============================================================================================================================================

    def LockDevicePanel(self):
        """
        PySDS [LockDevicePanel] : Lock the device front panel to prevent any actions of the user

        WARNING : This command seems to exhibit some weird response and no action at all on an SDS824X-HD

            Arguments :
                None

            Returns :
                self.GetAllErrors() : List of errors
        """
        self.__instr__.write("LOCK ON")
        return self.GetAllErrors()

    def UnlockDevicePanel(self):
        """
        PySDS [UnlockDevicePanel] : Unlock the device front panel to enable any actions of the user

        WARNING : This command seems to exhibit some weird response and no action at all on an SDS824X-HD

            Arguments :
                None

            Returns :
                self.GetAllErrors() : List of errors
        """
        self.__instr__.write("LOCK OFF")
        return self.GetAllErrors()

    def GetDevicePanelLockState(self):
        """
        PySDS [GetDevicePanelLockState] : Return the status of the lock on the front panel

        WARNING : This command seems to exhibit some weird response and no action at all on an SDS824X-HD

            Arguments :
                None

            Returns :
                Boolean : Lock (True) or not (False)
        """
        Ret = self.__instr__.query("LOCK?").strip().split(" ")[-1]
        if Ret == "ON":
            return True
        return False

    def RecallPreset(self, PresetNumber: int):
        """
        PySDS [RecallPreset] :  Apply a previously stored list of settings on the device.
                                Can only be called after the call of SavePreset function !
                                If 0 is passed, this is the default config.

            Argument :
                PresentNumber : Integer of the position to store the preset

            Returns :
                self.GetAllErrors() returns (List of errors)
                or
                -1 : Invalid preset ID
        """
        if PresetNumber > 20 or PresetNumber < 0:
            return [1, -1]

        self.__instr__.write(f"*RCL {PresetNumber}")
        return self.GetAllErrors()

    def SavePresent(self, PresetNumber: int):
        """
        PySDS [SavePresent] :   Store the settings of the device into a defined non volatile memory location.
                                Number 0 is not valid, since this location is the default preset.

            Argument :
                PresentNumber : Integer of the position to store the preset

            Returns :
                self.GetAllErrors() returns (List of errors)
                or
                -1 : Invalid preset ID
        """
        if PresetNumber > 20 or PresetNumber < 1:
            return [1, -1]

        self.__instr__.write(f"*SAV {PresetNumber}")
        return self.GetAllErrors()

    def ResetDevice(self):
        """
        PySDS [ResetDevice] : Perform a software reset of the device

        Arguments :
            None

        Returns :
            self.GetAllErrors() returns (List of errors)
        """

        self.__instr__.write("*RST")
        return self.GetAllErrors()

    # =============================================================================================================================================
    """
    Now, let's define some more advanced functions that will call some previously defined ones.

    It's more aimed at the user, even if the previous ones remains accessibles, since theses functions will provide more content.
    
    """
    # =============================================================================================================================================

    def GetAllErrors(self):
        """
        PySDS [GetAllErrors] :  Read the device errors, and until at least one error exist, continue to read it.
                                For each errors, it will be printed in console and returned on a list, with it's lengh in first position.

                                This function also trigger a reading of the status of the device to detect if value where adapted or cancelled.

            Arguments :
                None

            Returns :
                List :
                    Index 0 :       Number of errors that occured
                    Index 1 - n :   Device errors codes
        """

        FetchNextError = True
        Errors = [0]

        # For each loop, we ask the device an error
        # If not 0, then we parse it and add it to the list
        # When the last error has been fetched (or no errors at all !), we exit the loop

        while FetchNextError:
            Ret = self.__Generics__.ReadEXR()

            if Ret == 0:
                FetchNextError = False

            else:
                Errors[0] += 1
                Errors.append(int(Ret))

                # Theses errors messages came from the Siglent SCPI documentation, and are only here to help the developper to get the error easily !
                match Ret:
                    case 21:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Permission error. The command cannot be executed in local mode."
                        )
                    case 22:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Environment error. The instrument is not configured to correctly process command. For instance, the oscilloscope cannot be set to RIS at a slow timebase."
                        )
                    case 23:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Option error. The command applies to an option which has not been installed."
                        )
                    case 25:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Parameter error. Too many parameters specified."
                        )
                    case 26:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Non-implemented command."
                        )
                    case 32:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Waveform descriptor error. An invalid waveform descriptor has been detected."
                        )
                    case 36:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Panel setup error. An invalid panel setup data block has been detected."
                        )
                    case 50:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) No mass storage present when user attempted to access it."
                        )
                    case 53:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Mass storage was write protected when user attempted to create, or a file, to delete a file, or to format the device."
                        )
                    case 58:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Mass storage file not found."
                        )
                    case 59:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Requested directory not found."
                        )
                    case 61:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Mass storage filename not DOS compatible, or illegal filename."
                        )
                    case 62:
                        print(
                            f"     [ PySDS ] [ GetAllErrors ] : ({Ret}) Cannot write on mass storage because filename already exists."
                        )

        # When the loop exist, we return the list
        Retval = self.GetDeviceStatus()

        if Retval != 0:
            Errors[0] += 1
            Errors.append(
                Retval + 1000
            )  # Increment of 1000 to signify an error in the MSB register

        return Errors

    def GetDeviceStatus(self):
        """
        PySDS [GetDeviceStatus] :   Get the device status, and parse it to make it easier to use for developpers or users.
                                    Print each status bit

            Argument :
                None

            Returns :
                List of lenght 16, for each bit
        """

        # Fetch the value
        Ret = self.__Generics__.ReadINR()

        # Mask each bit in the range.
        # We do this by logic AND and shifting to get back to 0 | 1
        Bits = []
        for power in range(16):
            Bits.append((Ret & pow(2, power)) >> power)

        print("Device status :")
        print("Bit | Status | Message")
        for index, bit in enumerate(Bits):
            match index:
                case 0:
                    message = "A new signal has been acquired"
                case 1:
                    message = "A screen dump has terminated"
                case 2:
                    message = "A return to the local state is detected"
                case 3:
                    message = "A time-out has occurred in a data block transfer"
                case 4:
                    message = "A segment of a sequence waveform has been acquired"
                case 5:
                    message = "Reserved for LeCroy use"
                case 6:
                    message = 'Memory card, floppy or hard disk has become full in "AutoStore Fill" mode'
                case 7:
                    message = (
                        "A memory card, floppy or hard disk exchange has been detected"
                    )
                case 8:
                    message = "Waveform processing has terminated in Trace A"
                case 9:
                    message = "Waveform processing has terminated in Trace B"
                case 10:
                    message = "Waveform processing has terminated in Trace C"
                case 11:
                    message = "Waveform processing has terminated in Trace D"
                case 12:
                    message = "Pass/Fail test detected desired outcome"
                case 13:
                    message = "Trigger is ready"
                case 14:
                    message = "Reserved for future use"
                case 15:
                    message = "Reserved for future use"

            if bit == 1:
                print(f" {index:2} |  {bit:5} | {message}")
            else:
                print(f" {index:2} |  {bit:5} | -")

        return Bits

    def GetDeviceOptions(self):
        """
        PySDS [GetDeviceOptions] :  Return the list of the installed device options.
                                    Function isn't working for now, but the response seems correct.
                                    --> Return 0 where it shall return OPC 0...

            Arguments :
                None

            Returns :
                List of String for all options
        """

        Ret = self.__Generics__.ReadOPT()
        return Ret.split(" ")[-1].split(",")

    def GetDeviceStatus(self):
        """
        PySDS [GetDeviceStatus] :   Read the device status, and parse it to be easier for the user to read !

            Arguments :
                None

            Returns :
                List of lenght 16, for each bit
        """

        # Fetch the value
        Ret = self.__Generics__.ReadSTB()

        # Mask each bit in the range.
        # We do this by logic AND and shifting to get back to 0 | 1
        Bits = []
        for power in range(8):
            Bits.append((Ret & pow(2, power)) >> power)

        print("Device status register :")
        print("Bit | Status | Message")
        for index, bit in enumerate(Bits):
            match index:
                case 0:
                    message = "An enabled Internal state change has occurred"
                case 1:
                    message = "Reserved"
                case 2:
                    message = "A command data value has been adapted"
                case 3:
                    message = "Reserved"
                case 4:
                    message = "Output queue is not empty "
                case 5:
                    message = "An ESR enabled event has occurred"
                case 6:
                    message = "At least 1 bit in STB masked by SRE is one service is requested"
                case 7:
                    message = "Reserved for future use"

            if bit == 1:
                print(f" {index:2} |  {bit:5} | {message}")
            else:
                print(f" {index:2} |  {bit:5} | -")

        return Bits
