# ============================================================================================================
# Generics.py
# lheywang on 21/12/2024
#
# Base file for the generics SCPI class.
# This class could easily be reused with any IEEE 488.1 compliant device.
#
# ============================================================================================================


class SCPIGenerics:
    def __init__(self, instr, baseclass):
        self.__instr__ = instr
        self.__baseclass__ = baseclass

    def ClearStatus(self):
        """
        PySDS [ClearStatus] :   Clear the status register

            Arguments :
                None

            Returns :
                None
        """

        self.__instr__.write("*CLS")
        return

    def ReadCMR(self):
        """
        PySDS [ReadCMR] :   Read and clear the CMR register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("CMR?")
        return int(Ret.strip().split(" ")[-1])

    def ReadDDR(self):
        """
        PySDS [ReadDDR] :   Read and clear the DDR register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("DDR?")
        return int(Ret.strip().split(" ")[-1])

    def ReadESE(self):
        """
        PySDS [ReadESE] :   Read and clear the ESE register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("*ESE?")
        return int(Ret.strip())

    def ReadESR(self):
        """
        PySDS [ReadESR] :   Read and clear the ESE register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("*ESR?")
        return int(Ret.strip())

    def ReadEXR(self):
        """
        PySDS [ReadEXR] :   Read and clear the EXR register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        Ret = self.__instr__.query("EXR?")
        return int(Ret.strip().split(" ")[-1])

    def ReadIDN(self):
        """
        PySDS [ReadIDN] :   Read back the device name

            Arguments :
                None

            Returns :
                String : The output of the command
        """

        return self.__instr__.query("*IDN?").strip()

    def ReadINR(self):
        """
        PySDS [ReadINR] :   Read and clear the device status

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        return int(self.__instr__.query("INR?").strip().split(" ")[-1])

    def ReadOPC(self):
        """
        PySDS [ReadOPC] :   Read the Operation Complete status bit.
                            Actually, this function always return 1, because the device respond when the operation is complete...

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        return int(self.__instr__.query("*OPC?").strip())

    def ReadOPT(self):
        """
        PySDS [ReadOPT] :   Read the installed options on the device

            Arguments :
                None

            Returns :
                String : The output of the command
        """

        return self.__instr__.query("*OPT?").strip()

    def ReadSRE(self):
        """
        PySDS [ReadSRE] :   Read the service request enable register value

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        return int(self.__instr__.query("*SRE?").strip())

    def ReadSTB(self):
        """
        PySDS [ReadSTB] :   Read the status register

            Arguments :
                None

            Returns :
                Integer : Register value
        """

        return int(self.__instr__.query("*STB?").strip())

    def SetESE(self, value: int):
        """
        PySDS [SetESE] :   Write the ESE Register

            Arguments :
                Integer : Value to be written

            Returns :
                self.GetAllErrors() returns (List of errors)
        """

        if value > 255 or value < 0:
            print("     [ PySDS ] [ SetESE ] : Incorrect value passed !")
            return -1

        self.__instr__.write(f"*ESE {value}")
        return self.__baseclass__.GetAllErrors()

    def SetESR(self, value: int):
        """
        PySDS [SetESR] :   Write the ESR Register

            Arguments :
                Integer : Value to be written

            Returns :
                self.GetAllErrors() returns (List of errors)
        """

        if value > 128 or value < 0:
            print("     [ PySDS ] [ SetESR ] : Incorrect value passed !")
            return -1

        self.__instr__.write(f"*ESR {value}")
        return self.__baseclass__.GetAllErrors()

    def SetOPC(self):
        """
        PySDS [SetOPC] :   Write the OPC (Operation Complete) Status bit

            Arguments :
                None

            Returns :
                self.GetAllErrors() returns (List of errors)
        """
        self.__instr__.write("*OPC")
        return self.__baseclass__.GetAllErrors()

    def SetSRE(self, value: int):
        """
        PySDS [SetSRE] :   Write the ESR Register (Service Request Enable Register)

            Arguments :
                Integer : Value to be written

            Returns :
                self.GetAllErrors() returns (List of errors)
        """

        if value > 256 or value < 0:
            print("     [ PySDS ] [ SetSRE ] : Incorrect value passed !")
            return -1

        self.__instr__.write(f"*SRE {value}")
        return self.__baseclass__.GetAllErrors()