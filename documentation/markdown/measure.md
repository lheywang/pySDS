<a id="measure"></a>

# measure

<a id="measure.measure"></a>

# measure.measure

<a id="measure.measure.SiglentMeasure"></a>

## SiglentMeasure Objects

```python
class SiglentMeasure(SiglentBase)
```

pySDS [Files][SiglentMeasure] : Class herited from SiglentBase.
                                Store all command related the control of automated measures

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (14):
            GetSignalFrequency :            Get triggering signal frequency
            SetDelayMeasure :               Configure delay measure
            GetDelayMeasure :               Read delay measure
            SetMeasure :                    Configure measure
            GetMeasure :                    Read measure
            EnableMeasureStatistics :       Enable statistics
            DisableMeasureStatistics :      Disable statistics
            ResetMeasureStatistics :        Reset statistics
            RemoveMeasures :                Remove all measures
            GetStatsMeasure :               Read measures (with statistics)
            EnableMeasureGating :           Enable measure gating (restraint the measure to a part of the waveform)
            DisableMeasureGating :          Disable measure gating
            SetGatingLowerLimit :           Configure lower limit for gating
            SetGatingHigherLimit :          Configure higher limit for gating

<a id="measure.measure.SiglentMeasure.GetSignalFrequency"></a>

#### GetSignalFrequency

```python
def GetSignalFrequency()
```

pySDS [Measure][GetSignalFrequency] : Get the number of trigger crossing per seconds, in Hz.

WARNING : Measure only the trigger channel.

    Arguments :
        None

    Returns :
        Measure, in Hz.

<a id="measure.measure.SiglentMeasure.SetDelayMeasure"></a>

#### SetDelayMeasure

```python
def SetDelayMeasure(Type: str, Channel1: SiglentChannel,
                    Channel2: SiglentChannel)
```

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

<a id="measure.measure.SiglentMeasure.GetDelayMeasure"></a>

#### GetDelayMeasure

```python
def GetDelayMeasure(Type: str, Channel1: SiglentChannel,
                    Channel2: SiglentChannel)
```

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

<a id="measure.measure.SiglentMeasure.SetMeasure"></a>

#### SetMeasure

```python
def SetMeasure(Type: str, Channel: SiglentChannel)
```

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

<a id="measure.measure.SiglentMeasure.GetMeasure"></a>

#### GetMeasure

```python
def GetMeasure(Type: str, Channel: SiglentChannel)
```

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

<a id="measure.measure.SiglentMeasure.EnableMeasureStatistics"></a>

#### EnableMeasureStatistics

```python
def EnableMeasureStatistics()
```

pySDS [Measure][EnableMeasureStatistics] : Enable measurement stats

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="measure.measure.SiglentMeasure.DisableMeasureStatistics"></a>

#### DisableMeasureStatistics

```python
def DisableMeasureStatistics()
```

pySDS [Measure][DisableMeasureStatistics] : Disable measurement stats

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="measure.measure.SiglentMeasure.ResetMeasureStatistics"></a>

#### ResetMeasureStatistics

```python
def ResetMeasureStatistics()
```

pySDS [Measure][ResetMeasureStatistics] : Reset measurement stats values

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="measure.measure.SiglentMeasure.RemoveMeasures"></a>

#### RemoveMeasures

```python
def RemoveMeasures()
```

pySDS [Measure][RemoveMeasures] : Remove installed measures

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="measure.measure.SiglentMeasure.GetStatsMeasure"></a>

#### GetStatsMeasure

```python
def GetStatsMeasure(MeasureID)
```

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

<a id="measure.measure.SiglentMeasure.EnableMeasureGating"></a>

#### EnableMeasureGating

```python
def EnableMeasureGating()
```

pySDS [Measure][EnableMeasureGating] : Enable measurement gating, to only consider a small part of the waveform

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="measure.measure.SiglentMeasure.DisableMeasureGating"></a>

#### DisableMeasureGating

```python
def DisableMeasureGating()
```

pySDS [Measure][DisableMeasureGating] : Disable measurement gating.

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="measure.measure.SiglentMeasure.SetGatingLowerLimit"></a>

#### SetGatingLowerLimit

```python
def SetGatingLowerLimit(Time: float)
```

pySDS [Measure][SetGatingLowerLimit] : Set lower gating time.

WARNING : This value can't be greater than Higher limit. No checks are done !

    Arguments :
        Time : Value of time to be used, in seconds.

    Returns :
        self.GetAllErrors()

<a id="measure.measure.SiglentMeasure.SetGatingHigherLimit"></a>

#### SetGatingHigherLimit

```python
def SetGatingHigherLimit(Time: float)
```

pySDS [Measure][SetGatingLowerLimit] : Set higher gating time.

WARNING : This value can't be lower than Lower limit. No checks are done !

    Arguments :
        Time : Value of time to be used, in seconds.

    Returns :
        self.GetAllErrors()

