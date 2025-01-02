# ============================================================================================================
# Measure.py
# lheywang on 21/12/2024
#
# Base file for the measure class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel


class SiglentMeasure(SiglentBase):
    """
    pySDS [Files][SiglentMeasure] : Class herited from SiglentBase.
                                    Store all command related the control of automated measures

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (7):
    """

    def GetSignalFrequency(self):
        """
        pySDS [Measure][GetSignalFrequency] : Get the number of trigger crossing per seconds, in Hz.

        WARNING : Measure only the trigger channel.

            Arguments :
                None

            Returns :
                Measure, in Hz.
        """
        ret = self.__instr__.query("CYMT?").strip().split(" ")[-1]

        if "E" in ret:
            # Notation 1 (seems newer ?)
            return float(ret[:-2])
        else:
            if "<" in ret:
                # Some old notation are <10Hz, with is casted to 10 and returned like that.
                # They removed it in the newest devices, with then use the parsing.
                return 10.00

            val = ret.replace("k", "").replace("M", "")
            val = float(val[:-2].strip())

            if "k" in ret:
                return val * 1_000
            if "M" in ret:
                return val * 1_000_000
            return val

    def SetDelayMeasure(
        self, Type: str, Channel1: SiglentChannel, Channel2: SiglentChannel
    ):
        """
        pySDS [Measure][SetDelayMeasure] : Configure a time related measurement

        WARNING : This function shall be called before calling the Get function.

            Arguments :
                Type :      Type of mesure. PHA | FRR | FRF | FFR | FFF | LRR | LRF | LFR | LFF | SKEW
                Channel1 :  Siglent channel for the source 1
                Channel2 :  Siglent channel for the source 2

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid type
                -2 : Invalid Channel1 class
                -3 : Invalid Channel2 class

            Available measures :
                PHA :The phase difference between two channels. (rising edge - rising edge)
                FRR Delay between two channels. (first rising edge - first rising edge)
                FRF Delay between two channels. (first rising edge - first falling edge)
                FFR Delay between two channels. (first falling edge - first rising edge)
                FFF Delay between two channels. (first falling edge - first falling edge)
                LRR Delay between two channels. (first rising edge - last rising edge)
                LRF Delay between two channels. (first rising edge - last falling edge)
                LFR Delay between two channels. (first falling edge - last rising edge)
                LFF Delay between two channels. (first falling edge - last falling edge)
                SKEW Delay between two channels. (edge to edge of the same type)
        """
        if Type not in [
            "PHA",
            "FRR",
            "FRF",
            "FFR",
            "FFF",
            "LRR",
            "LRF",
            "LFR",
            "LFF",
            "SKEW",
        ]:
            return [1, -1]
        if type(Channel1) is not type(SiglentChannel):
            return [1, -2]
        if type(Channel2) is not type(SiglentChannel):
            return [1, -3]

        self.__instr__.write(
            f"MEAD {Type},{Channel1.__channel__}-{Channel2.__channel__}:"
        )
        return self.__baseclass__.GetAllErrors()

    def GetDelayMeasure(
        self, Type: str, Channel1: SiglentChannel, Channel2: SiglentChannel
    ):
        """
        pySDS [Measure][GetDelayMeasure] : Read the value of a measure (and maybe set it ??)

            Arguments :
                Type :      Type of mesure. (See list linked)
                Channel1 :  SiglentChannel for the source 1
                Channel2 :  SiglentChannel for the source 2

            Returns :
                The value read, or if negative :
                -1 : Invalid type
                -2 : Invalid Channel1 class
                -3 : Invalid Channel2 class

            Available measures :
                PHA :The phase difference between two channels. (rising edge - rising edge)
                FRR Delay between two channels. (first rising edge - first rising edge)
                FRF Delay between two channels. (first rising edge - first falling edge)
                FFR Delay between two channels. (first falling edge - first rising edge)
                FFF Delay between two channels. (first falling edge - first falling edge)
                LRR Delay between two channels. (first rising edge - last rising edge)
                LRF Delay between two channels. (first rising edge - last falling edge)
                LFR Delay between two channels. (first falling edge - last rising edge)
                LFF Delay between two channels. (first falling edge - last falling edge)
                SKEW Delay between two channels. (edge to edge of the same type)
        """
        if Type not in [
            "PHA",
            "FRR",
            "FRF",
            "FFR",
            "FFF",
            "LRR",
            "LRF",
            "LFR",
            "LFF",
            "SKEW",
        ]:
            return -1
        if type(Channel1) is not type(SiglentChannel):
            return -2
        if type(Channel2) is not type(SiglentChannel):
            return -3

        ret = (
            self.__instr__.query(
                f"{Channel1.__channel__}-{Channel2.__channel__}:MEAD? {Type}"
            )
            .strip()
            .split(",")[-1]
        )
        if "S" in ret:
            # Handle timings
            return float(ret.replace("S", ""))
        else:
            # Handle degrees
            return float(ret.replace("degree", ""))

    def SetMeasure(self, Type: str, Channel: SiglentChannel):
        """
        pySDS [Measure][SetMeasure] : Install a new measure

            Arguments :
                Type :      The measure to be done (see list at the end of the doc)
                Channel :   SiglentChannel to be measured

            Returns :
                self.GetAllErrors()
                or
                -1 : Invalid type
                -2 : Invalid Channel type

            Available measures :
                PKPK : vertical peak-to-peak
                MAX : maximum vertical value
                MIN : minimum vertical value
                AMPL : vertical amplitude
                TOP : waveform top value
                BASE : waveform base value
                CMEAN : average value in the first cycle
                MEAN : average value
                STDEV : standard deviation of the data
                VSTD : standard deviation of the data in the first cycle
                RMS : RMS value
                CRMS : RMS value in the first cycle
                OVSN : overshoot of a falling edge
                FPRE : preshoot of a falling edge
                OVSP : overshoot of a rising edge
                RPRE : preshoot of a rising edge
                LEVELX : Level measured at trigger position
                PER : period
                FREQ : frequency
                PWID : positive pulse width
                NWID : negative pulse width
                RISE : rise-time
                FALL : fall-time
                WID : Burst width
                DUTY : positive duty cycle
                NDUTY : negative duty cycle
                DELAY : time from the trigger to the first transition at the 50% crossing
                TIMEL : time from the trigger to each rising edge at the 50% crossing
                ALL : All measurements snapshot, equal to turn on the switch of all measure
        """
        if Type not in [
            "PKPK",
            "MAX",
            "MIN",
            "AMPL",
            "TOP",
            "BASE",
            "CMEAN",
            "MEAN",
            "STDEV",
            "VSTD",
            "RMS",
            "CRMS",
            "OVSN",
            "FPRE",
            "OVSP",
            "RPRE",
            "LEVELX",
            "PER",
            "FREQ",
            "PWID",
            "NWID",
            "RISE",
            "FALL",
            "WID",
            "DUTY",
            "NDUTY",
            "DELAY",
            "TIMEL",
            "ALL",
        ]:
            return [1, -1]
        if type(Channel) is not type(SiglentChannel):
            return [1, -2]

        self.__instr__.write(f"PACU {Type},{Channel.__channel__}")
        return self.__baseclass__.GetAllErrors()

    def GetMeasure(self, Type: str, Channel: SiglentChannel):
        """
        pySDS [Measure][GetMeasure] : Read a measure

            Arguments :
                Type :      The measure to be done (see list at the end of the doc)
                Channel :   SiglentChannel to be measured

            Returns :
                dict with measure name and value.
                Errors are reaturned under the error key.

            Available measures :
                PKPK : vertical peak-to-peak
                MAX : maximum vertical value
                MIN : minimum vertical value
                AMPL : vertical amplitude
                TOP : waveform top value
                BASE : waveform base value
                CMEAN : average value in the first cycle
                MEAN : average value
                STDEV : standard deviation of the data
                VSTD : standard deviation of the data in the first cycle
                RMS : RMS value
                CRMS : RMS value in the first cycle
                OVSN : overshoot of a falling edge
                FPRE : preshoot of a falling edge
                OVSP : overshoot of a rising edge
                RPRE : preshoot of a rising edge
                LEVELX : Level measured at trigger position
                PER : period
                FREQ : frequency
                PWID : positive pulse width
                NWID : negative pulse width
                RISE : rise-time
                FALL : fall-time
                WID : Burst width
                DUTY : positive duty cycle
                NDUTY : negative duty cycle
                DELAY : time from the trigger to the first transition at the 50% crossing
                TIMEL : time from the trigger to each rising edge at the 50% crossing
                ALL : All measurements snapshot, equal to turn on the switch of all measure
        """
        if Type not in [
            "PKPK",
            "MAX",
            "MIN",
            "AMPL",
            "TOP",
            "BASE",
            "CMEAN",
            "MEAN",
            "STDEV",
            "VSTD",
            "RMS",
            "CRMS",
            "OVSN",
            "FPRE",
            "OVSP",
            "RPRE",
            "LEVELX",
            "PER",
            "FREQ",
            "PWID",
            "NWID",
            "RISE",
            "FALL",
            "WID",
            "DUTY",
            "NDUTY",
            "DELAY",
            "TIMEL",
            "ALL",
        ]:
            return {"error": -1}
        if type(Channel) is not type(SiglentChannel):
            return {"error": -2}

        out = dict()
        ret = (
            self.__instr__.query(f"{Channel.__channel__}:PAVA? {Type}")
            .strip()
            .split(" ")[-1]
            .split(",")
        )
        for index, meas in enumerate(ret):
            # We need to handle naming and value for each
            if index % 2 == 0:
                key = meas
                val = ret[index + 1]

                # remove traling units
                while val[-1].isalpha():
                    val = val[:-1]

                if "*" in val:
                    val = 0.00

                val = float(val)
                out[key] = val
            else:
                # Continue the loop. We're not right
                continue
        return out

    def EnableMeasureStatistics(self):
        """
        pySDS [Measure][EnableMeasureStatistics] : Enable measurement stats

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PASTAT ON")
        return self.__baseclass__.GetAllErrors()

    def DisableMeasureStatistics(self):
        """
        pySDS [Measure][DisableMeasureStatistics] : Disable measurement stats

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PASTAT OFF")
        return self.__baseclass__.GetAllErrors()

    def ResetMeasureStatistics(self):
        """
        pySDS [Measure][ResetMeasureStatistics] : Reset measurement stats values

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PASTAT RESET")
        return self.__baseclass__.GetAllErrors()

    def RemoveMeasures(self):
        """
        pySDS [Measure][RemoveMeasures] : Remove installed measures

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("PASTAT")
        return self.__baseclass__.GetAllErrors()

    def GetStatsMeasure(self, MeasureID):
        """
        pySDS [Measure][GetStatsMeasure] : Read the statistics for a measure.

        WARNING : This function need statistics to be enabled !
        WARNING2 : The ID of the measure

            Arguments :
                NumberOfMeasures : The number of measured stats wanted.

            Returns :
                dict with measure name and value.
                Errors are reaturned under the error key.

            Errors codes :
                -1 : Invalid Number of measures. Must be between 1 and 5

        """
        if MeasureID < 0 or MeasureID > 5:
            return {"errors": -1}

        out = dict()
        ret = (
            self.__instr__.query(f"PAVA? STAT{MeasureID}").strip().split(" ")[2:]
        )  # Two last elements
        out["channel"] = ret[0]

        measures = ret[1].split(":")
        out["type"] = measures[0]

        values = measures[1].split(",")

        for index, meas in enumerate(values):
            # We need to handle naming and value for each
            if index % 2 == 0:
                key = meas
                val = values[index + 1]

                # remove traling units
                while val[-1].isalpha():
                    val = val[:-1]

                if "*" in val:
                    val = 0.00

                val = float(val)
                out[key] = val
            else:
                # Continue the loop. We're not on the correct index
                continue
        return out

    def EnableMeasureGating(self):
        """
        pySDS [Measure][EnableMeasureGating] : Enable measurement gating, to only consider a small part of the waveform

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("MEGS ON")
        return self.__baseclass__.GetAllErrors()

    def DisableMeasureGating(self):
        """
        pySDS [Measure][DisableMeasureGating] : Disable measurement gating.

            Arguments :
                None

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write("MEGS OFF")
        return self.__baseclass__.GetAllErrors()

    def SetGatingLowerLimit(self, Time: float):
        """
        pySDS [Measure][SetGatingLowerLimit] : Set lower gating time.

        WARNING : This value can't be greater than Higher limit. No checks are done !

            Arguments :
                Time : Value of time to be used, in seconds.

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"MEGA {Time}")
        return self.__baseclass__.GetAllErrors()

    def SetGatingHigherLimit(self, Time: float):
        """
        pySDS [Measure][SetGatingLowerLimit] : Set higher gating time.

        WARNING : This value can't be lower than Lower limit. No checks are done !

            Arguments :
                Time : Value of time to be used, in seconds.

            Returns :
                self.GetAllErrors()
        """
        self.__instr__.write(f"MEGB {Time}")
        return self.__baseclass__.GetAllErrors()
