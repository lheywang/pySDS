# ============================================================================================================
# Cursor.py
# lheywang on 19/12/2024
#
# Base file for the cursor class
#
# ============================================================================================================

from datetime import datetime

class DATE:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass

    def GetDate(self):
        """
        PySDS [GetDate] :   Read and return the date stored on the oscilloscope RTC

        Actually, this function does not work, despite that it's presence is stated on the datasheet.
        --> Possible issues :
                Function non implemented ?
                Syntax not OK ?

            Arguments :
                None

            Returns :
                Python Datetime object
        """

        Ret = self.__instr__.query("DATE?")
        Ret = Ret.strip().split(" ")[1:]

        # Why did they express month like that ? Cannot they send the number ?
        match Ret[1]:
            case "JAN":
                month = 1
            case "FEB":
                month = 2
            case "MAR":
                month = 3
            case "APR":
                month = 4
            case "MAY":
                month = 5
            case "JUN":
                month = 6
            case "JUL":
                month = 7
            case "AUG":
                month = 8
            case "SEP":
                month = 9
            case "OCT":
                month = 10
            case "NOV":
                month = 11
            case "DEC":
                month = 12

        return datetime(Ret[2], month, Ret[0], Ret[3], Ret[4], Ret[5])

    def SetDate(self, Date: datetime):
        """
        PySDS [SetDate] :   Set the internal RTC date and time

            Arguments :
                Python Datetime object

            Returns :
                self.GetAllErrors() returns (List of errors)
        """
        self.__instr__.write(
            f"DATE {Date.day},{Date.strftime("%b").upper()},{Date.year},{Date.hour},{Date.minute},{Date.second}"
        )
        return self.__baseclass__.GetAllErrors()