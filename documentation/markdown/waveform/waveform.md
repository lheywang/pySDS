<a id="waveform"></a>

# waveform

<a id="waveform.waveform"></a>

# waveform.waveform

<a id="waveform.waveform.SiglentWaveform"></a>

## SiglentWaveform Objects

```python
class SiglentWaveform(SiglentBase)
```

pySDS [Files][SiglentWaveform] :    Class herited from SiglentBase.
                                    Store all command related the control of waveform storage

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (1):
            GetWaveformData :       Read the waveform data

<a id="waveform.waveform.SiglentWaveform.GetWaveformData"></a>

#### GetWaveformData

```python
def GetWaveformData(Channel,
                    Vdiv=1,
                    Vos=0,
                    Tdiv=0.000_000_001,
                    SampleNumber=1000)
```

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

