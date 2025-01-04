<a id="channel"></a>

# channel

<a id="channel.channel"></a>

# channel.channel

<a id="channel.channel.SiglentChannel"></a>

## SiglentChannel Objects

```python
class SiglentChannel(SiglentBase)
```

pySDS [Channel][SiglentChannel] :   Class herited from SiglentBase.
                                    Store all command related to a channel
    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (12):
            SetAttenuation :            Configure channel attenuation
            EnableBandwithFilter :      Enable 20 MHz filter on the channel
            DisableBandwithFilter :     Disable 20 MHz filter on the channel
            SetCoupling :               Configure channel coupling
            SetOffset :                 Configure channel offset
            SetSkew :                   Configure channel skew
            EnableTrace :               Enable trace draw on the screen
            DisableTrace :              Disable trace draw on the screen
            SetTraceUnit :              Configure trace unit
            SetTraceDIV :               Configure trace gain
            EnableTraceInvert :         Enable inversion of the trace
            DisableTraceInvert :        Disable inversion of the trace

<a id="channel.channel.SiglentChannel.__init__"></a>

#### \_\_init\_\_

```python
def __init__(instr, baseclass, channel, impedance)
```

Overhide the standard class init to store some more advanced data !

Check SiglentBase doc before !

Added attributes :
    Private (2) :
        __channel__ :   Descriptor of the channel
        __impedance__ : List of supported impedance for this channel

    Public (0) :
        None

Added methods :
    Private (0) :
        None

    Public (0) :
        None

<a id="channel.channel.SiglentChannel.SetAttenuation"></a>

#### SetAttenuation

```python
def SetAttenuation(Value)
```

pySDS [Channel][SetAttenuation] : Configure the probe attenuation

    Arguments :
        Value : The attenuation value, between 0.1 and 10000 (checked against a list of values)

    Returns :
        self.GetAllErrors()

<a id="channel.channel.SiglentChannel.EnableBandwithFilter"></a>

#### EnableBandwithFilter

```python
def EnableBandwithFilter()
```

pySDS [Channel][EnableBandwithFilter] : Enable a 20 Mhz low pass filter on the channel. Used to rejet high frequency noise.

    Arguments :
        None__

    Returns :
        self.GetAllErrors()

<a id="channel.channel.SiglentChannel.DisableBandwithFilter"></a>

#### DisableBandwithFilter

```python
def DisableBandwithFilter()
```

pySDS [Channel][DisableBandwithFilter] : Disable a 20 Mhz low pass filter on the channel.

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="channel.channel.SiglentChannel.SetCoupling"></a>

#### SetCoupling

```python
def SetCoupling(ACDC="D", Impedance=1000000)
```

pySDS [Channel][SetCoupling] : Set the channel coupling mode.

    Arguments :
        ACDC : Mode of coupling, AC or DC (AC rejet any DC signal). Values are A | D
        Impedance : Impedance of input. Warning : Some device doesn't support de 50 Ohm coupling !

    Returns :
        self.GetAllErrors()
        or
        "-1" : Incorrect coupling
        "-2" : Incorrect impedance

<a id="channel.channel.SiglentChannel.SetOffset"></a>

#### SetOffset

```python
def SetOffset(Offset: float)
```

pySDS [Channel][SetOffset] : Configure the offset used.

    Arguments :
        Offset, in volts

    Returns :
        self.GetAllErrors()

<a id="channel.channel.SiglentChannel.SetSkew"></a>

#### SetSkew

```python
def SetSkew(Skew: int)
```

pySDS [Channel][SetSkew] : Configure the delay between each channels, to compensate cable lenght matching

    Arguments :
        Skew : +- 100 ns to be applied

    Returns :
        self.GetAllErrors()
        or
        [1, -1] if Skew is not valid !

<a id="channel.channel.SiglentChannel.EnableTrace"></a>

#### EnableTrace

```python
def EnableTrace()
```

pySDS [Channel][EnableTrace] : Enable the draw of the trace on the screen

    Arguments :
        None

    Return :
        self.GetAllErrors()

<a id="channel.channel.SiglentChannel.DisableTrace"></a>

#### DisableTrace

```python
def DisableTrace()
```

pySDS [Channel][EnableTrace] : Disable the draw of the trace on the screen

    Arguments :
        None

    Return :
        self.GetAllErrors()

<a id="channel.channel.SiglentChannel.SetTraceUnit"></a>

#### SetTraceUnit

```python
def SetTraceUnit(Unit: str)
```

pySDS [Channel][SetTraceUnit] : Configure if the trace is on V (Volt) or A (Ampere)

    Arguments :
        Unit : V | A

    Returns :
        self.GetAllErrors()

<a id="channel.channel.SiglentChannel.SetTraceDIV"></a>

#### SetTraceDIV

```python
def SetTraceDIV(Div: float)
```

pySDS [Channel][SetTraceVDIV] : Configure the gain on the unit of the trace, from 500E-6 to 10

    Arguments :
        Div : Gain to be applied

    Returns :
        self.GetAllErrors()
        or
        or -1 if invalid value

<a id="channel.channel.SiglentChannel.EnableTraceInvert"></a>

#### EnableTraceInvert

```python
def EnableTraceInvert()
```

pySDS [Channel][EnableTraceInvert] : Enable invert the measure of the trace (* -1)

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="channel.channel.SiglentChannel.DisableTraceInvert"></a>

#### DisableTraceInvert

```python
def DisableTraceInvert()
```

pySDS [Channel][DisableTraceInvert] : Disable invert the measure of the trace (* -1)

    Arguments :
        None

    Returns :
        self.GetAllErrors()

