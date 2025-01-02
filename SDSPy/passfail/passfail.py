# ============================================================================================================
# Waveform.py
# lheywang on 21/12/2024
#
# Base file for the waveform class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel


class SiglentPassFail(SiglentBase):
    """
    pySDS [Files][SiglentPassFail] :    Class herited from SiglentBase.
                                        Store all command related the control of automated tests

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (14):
                ClearTests :                    Clear tests results
                EnableBuzzerOnFail :            Enable buzzer
                DisableBuzzerOnFail :           Disable buzzer
                CreateRule :                    Create new rule
                GetFramesResults :              Get results
                EnableInformationDisplay :      Show infos on screen
                DisableInformationDisplay :     Hide infos on screen
                EnablePassFailMode :            Enable mode
                DisablePassFailMode :           Disable mode
                EnableStopOnFail :              Enable stop on fail
                DisableStopOnFail :             Disable stop on fail
                Runtest :                       Run the test
                Stoptest :                      Stop the test
                SetSource :                     Set source
                SetTolerances :                 Configure tolerances
    """

    def ClearTests(self):
        """
        pySDS [PassFail][ClearTests] : Clear the results of the test

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PACL")
        return self.__baseclass__.GetAllErrors()

    def EnableBuzzerOnFail(self):
        """
        pySDS [PassFail][EnableBuzzerOnFail] : Enable the buzzer when a fail is detected

        WARNING : The documentation is not clear about the real usage of this function. Use at your own risks !

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFBF ON")
        return self.__baseclass__.GetAllErrors()

    def DisableBuzzerOnFail(self):
        """
        pySDS [PassFail][DisableBuzzerOnFail] : Disable the buzzer when a fail is detected

        WARNING : The documentation is not clear about the real usage of this function. Use at your own risks !

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFBF OFF")
        return self.__baseclass__.GetAllErrors()

    def CreateRule(self):
        """
        pySDS [PassFail][CreateRule] : Create a pass fail test around the selected channel.

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFCM")
        return self.__baseclass__.GetAllErrors()

    def GetFramesResults(self):
        """
        pySDS [PassFail][GetFramesResults] : Return the number of frames that passed the test, failed and total

            Arguments :
                None

            Returns :
                List of values : Failed, Passed, Total
        """
        ret = self.__instr__.query("PFDD?").strip().split(" ")[-1].split(",")
        return [int(ret[1]), int(ret[3]), int(ret[5])]

    def EnableInformationDisplay(self):
        """
        pySDS [PassFail][EnableInformationDisplay] : Enable on the screen the information panel

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFDS ON")
        return self.__baseclass__.GetAllErrors()

    def DisableInformationDisplay(self):
        """
        pySDS [PassFail][DisableInformationDisplay] : Disable on the screen the information panel

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFDS OFF")
        return self.__baseclass__.GetAllErrors()

    def EnablePassFailMode(self):
        """
        pySDS [PassFail][EnablePassFailMode] : Enable the pass/fail mode on the scope

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFEN ON")
        return self.__baseclass__.GetAllErrors()

    def DisablePassFailMode(self):
        """
        pySDS [PassFail][DisablePassFailMode] : Disable the pass/fail mode on the scope

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFEN OFF")
        return self.__baseclass__.GetAllErrors()

    def EnableStopOnFail(self):
        """
        pySDS [PassFail][EnableStopOnFail] : Stop the scope once the first fail has been detected

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFFS ON")
        return self.__baseclass__.GetAllErrors()

    def DisableStopOnFail(self):
        """
        pySDS [PassFail][DisableStopOnFail] : Do not stop the scope once the first fail has been detected

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFFS OFF")
        return self.__baseclass__.GetAllErrors()

    def Runtest(self):
        """
        pySDS [PassFail][RunTest] : Launch the test execution

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFOP ON")
        return self.__baseclass__.GetAllErrors()

    def Stoptest(self):
        """
        pySDS [PassFail][Stoptest] : Stop the test execution

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PFOP OFF")
        return self.__baseclass__.GetAllErrors()

    def SetSource(self, Channel: SiglentChannel):
        """
        pySDS [PassFail][SetSource] : Set the source for the selftest

            Arguments :
                Channel : SiglentChannel class to be used

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid channel descriptor
        """
        if type(Channel) is not type(SiglentChannel):
            return [1, -1]

        self.__instr__.write(f"PFSC {Channel.__channel__}")
        return self.__baseclass__.GetAllErrors()

    def SetTolerances(self, X, Y):
        """
        pySDS [PassFail][SetTolerances] : Set the X and Y tolerances for this source (Tolerances are expressed as on screen DIV)

            Arguments :
                X : X tolerance (between 0.04 and 4)
                Y : Y tolerance (between 0.04 and 4)

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid X tolerance
                -2 : Invalid Y tolerance
        """
        if X < 0.04 or X > 4:
            return [1, -1]
        if Y < 0.04 or Y > 4:
            return [1, -2]

        self.__instr__.write(
            f"PFST XMASK,{round(X / 0.04) * 0.04:.2f},YMASK{round(Y / 0.04) * 0.04:.2f}"
        )
        return self.__baseclass__.GetAllErrors()
