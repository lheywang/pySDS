# ============================================================================================================
# Waveform.py
# lheywang on 21/12/2024
#
# Base file for the waveform class
#
# ============================================================================================================
from BaseOptionnalClass import SiglentBase
from channel import SiglentChannel
from digital import SiglentDChannel


class SiglentWaveform(SiglentBase):
    """
    pySDS [Files][SiglentWaveform] :    Class herited from SiglentBase.
                                        Store all command related the control of waveform storage

        Attributes :
            Herited from SiglentBase

        Methods :
            Private (0) :
                None

            Public (1):
                GetWaveformData :       Read the waveform data
    """

    def GetWaveformData(self, Channel, Vdiv = 1, Vos = 0, Tdiv = 0.000_000_001, SampleNumber = 1000):
        """
        pySDS [Waveform][GetWaveformData] : Return the raw data for a waveform

        WARNING :   Due to high complexity in the formulaes, this function set the export to it's own settings (max number of points !)
                    Otherwise, this would cause issues on the parsing of timebases and so...

            Arguments :
                Channel :   Channel to be exported (Cx, Dx, MATH)
                Vdiv :      Voltage scale for the selected channel      Default to 1
                Vos :       Voltage offset for the selected channel     Default to 0
                Tdiv :      Timebase value                              Default to 1 ns
                SampleNumber : Number of sample in memory (SANU) :      Default to 1000

            Returns :
                List of points (Voltages)
                or
                -1000 : Invalid channel
                -1001 : Did not fetch the end of message
                -1002 : Fetched invalid header
                -1003 : Fetched wrong channel
                -1004 : Fetched incorrect number of bytes
        """
        # Ensure correct arguments
        if (
            type(Channel) is not SiglentChannel
            and type(Channel) is not SiglentDChannel
            and Channel is not "MATH"
        ):
            return [-1000], []
        
        # Configure the device
        self.__instr__.write("WFSU SP,0,NP,0,FP,0") # All data points

        # First, get the data
        self.__instr__.write(f"{Channel}:WF? DAT2")
        data = self.__instr__.read_raw()

        # Split data
        if Channel == "MATH":
            header = data[:23]
            wave = data[24:-2]
            end = data[-2:]
        else:
            header = data[:21]
            wave = data[22:-2]
            end = data[-2:]

        # End check
        if end[0] is not r"\n" and end[1] is not r"\n":
            return [-1001], []

        # Header check
        if Channel == "MATH":
            if header[4:15] is not ":WF DAT2,#9":
                return [-1002], []
            if header[:4] is not Channel[:4]:
                return [-1003], []
            data_len = int(header[16:])
        else:
            if header[2:13] is not ":WF DAT2,#9":
                return [-1002], []
            if header[:2] is not Channel[:2]:
                return [-1003], []
            data_len = int(header[13:])

        if len(wave) != data_len:
            return [-1004], []
        
        # Analog channel
        if header[0] == "C":
            # Now starting to decode the data
            out = []
            time = []
            for index, byte in enumerate(data):
                val = int(byte, 16)
                if val > 127:
                    val -= 256

                out.append(float(val * (Vdiv / 25) - Vos))
                time.append(float((-Tdiv * 7) + index  * Tdiv))

        # Digital channel
        elif header[0] == "D":
            # Now starting to decode the data
            out = []
            time = []
            for index, byte in enumerate(data):
                # Iterate over each bit
                for index2, bit in enumerate(format(int(byte, 16), '#010b')[2:]):
                    out.append(float(bit))
                    time.append(float((-Tdiv * 7) + (index * 8 + index2)  * Tdiv))

        # Maths data
        else:
             # Now starting to decode the data
            Tinterpol = data_len / SampleNumber * Tdiv

            out = []
            time = []
            for index, byte in enumerate(data):
                val = int(byte, 16)
                if val > 127:
                    val -= 256

                out.append(float(val * (Vdiv / 25) - Vos))
                time.append(float((-Tdiv * 7) + index  * Tinterpol))

