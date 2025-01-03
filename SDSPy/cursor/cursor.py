# ============================================================================================================
# Cursor.py
# lheywang on 19/12/2024
#
# Base file for the cursor class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel
from warnings import warn


class SiglentCursor(SiglentBase):
    """
    pySDS [Cursor][SiglentCursor] : Class herited from SiglentBase.
                                    Store all command related the control of cursors
        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (6):
                SetCursorMode :     Set the mode for a cursor
                GetCursorMode :     Read the mode of a cursor
                PlaceCursor :       Place a cursor
                GetPlacedCursor :   Return the placed cursor on a trace
                SetCursorType :     Configure the cursor type
                GetCursorValue :    Read the value of a cursor
    """

    def SetCursorMode(self, Mode):
        """
        pySDS [Cursor][SetCursorMode] : Set the mode of operation of the cursors

            Arguments :
                Mode :  The mode wanted between OFF | MANUAL | TRACK | (ON)
                        *ON is reserved to some legacy devices, it's usage will trigger a warning !

            Returns :
                self.GetAllErrors()
                or
                -1 if invalid mode has been passed
        """
        if Mode not in ["ON", "OFF", "TRACK", "MANUAL"]:
            return [1, -1]

        if Mode == "ON":
            warn(
                "      pySDS [Cursor][SetCursorMode] : Usage of a legacy mode has been done ! Check if it's correct !"
            )

        self.__instr__.write(f"CRMS {Mode}")
        return self.__baseclass__.GetAllErrors()

    def GetCursorMode(self):
        """
        pySDS [Cursor][GetCursorMode] : Return the mode of operation of the cursor

            Arguments :
                None

            Returns :
                Device response
        """
        return self.__instr__.query("CRMS?").strip().split(" ")[-1]

    def PlaceCursor(self, Channel: SiglentChannel, Cursor, Position):
        """
        pySDS [Cursor][PlaceCursor] : Place a cursor

        WARNING :   Each cursor is unique, you can't set twice the cursor on two different channels.
                    The device will consider the last call only.

        WARNING2 :  Some settings may trigger an out of bound error. Make sure to check the return code of this function.

            Arguments :
                Channel : The channel to which the cursor belong. This is a SiglentChannel class.
                Cursor : VREF | VDIF | TREF | TDIF | HREF | HDIF
                Position : Value where to place the cursor. This value is sensitive to errors and isn't check internally

            Returns :
                GetAllErrors() : Read and return all of the device errors
        """
        if Cursor not in ["VREF", "VDIF", "TDIF", "TREF", "HREF", "HDIF"]:
            return [1, -1]

        self.__instr__.write(f"{Channel.__channel__}:CRST {Cursor},{Position}")
        return self.__baseclass__.GetAllErrors()

    def GetPlacedCursor(self, Channel: SiglentChannel):
        """
        pySDS [Cursor][GetPlacedCursor] : Return the name of the cursor placed on a channel

            Arguments :
                Channel : The channel to which the cursor belong. This is a SiglentChannel class.

            Returns :
                List of cursor linked to this channel
        """
        return (
            self.__instr__.query(f"{Channel.__channel__}:CRST?")
            .strip()
            .split(" ")
            .split(",")
        )

    def SetCursorType(self, Type):
        """
        pySDS [Cursor][SetCursorType] : Configure the cursor type

            Arguments :
                Type : X | -X | Y | -Y

            Returns :
                Configured type
                or "-1" if wrong type passed
        """
        if Type not in ["X", "-X", "Y", "-Y"]:
            return [1, -1]

        self.__instr__.write(f"CRTY {Type}").strip().split(" ")[-1]
        return self.__baseclass__.GetAllErrors()

    def GetCursorValue(self, Channel: SiglentChannel, Mode):
        """
        pySDS [Cursor][GetCursorValue] : Return the values of a cursor

        WARNING : Make sure that a cursor has been placed on this channel, or the device will trigger an error :

            Arguments :
                Channel : The channel where the measure belong
                Mode : HREL | VREL ==> Read the horizontal or vertical measure

            Returns : (List of values)
                Delta
                (1 / Delta) : Only in HREL mode, 0 in VREL mode
                Value1
                Value2

                or
                [-err, -err, -err, -err] in case or error with err = errror code

            Errors code
                -1 : Error occured while running the command
        """

        ret = (
            self.__instr__.query(f"{Channel.__channel__}:CRVA? {Mode}")
            .strip()
            .split(" ")[-1]
            .split(",")
        )

        match ret[0]:
            case "HREL":
                return [float(ret[1]), float(ret[2]), float(ret[3]), float(ret[4])]
            case "VREL":
                return [float(ret[1]), 0.00, float(ret[2]), float(ret[3])]
            case _:  # default case
                return [-1] * 4
        return [-2, -2, -2, -2]  # shouldn't get here, and if we do, good luck !
