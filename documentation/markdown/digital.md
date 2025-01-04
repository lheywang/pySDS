<a id="digital"></a>

# digital

<a id="digital.digital"></a>

# digital.digital

<a id="digital.digital.SiglentDigital"></a>

## SiglentDigital Objects

```python
class SiglentDigital(SiglentBase)
```

pySDS [Digital][SiglentDigital] :   Class herited from SiglentBase.
                                    Store all command related the control of digital channels (scopes with MSO option only)

    WARNING :   This section of code is extremely undocumented, and the rare parts that are documentation aren't comprehesible.
                Take all of this code with salt, since bugs can exists here due to an error of my person, or an error of the doc, or both
                If something went bugging here, you can report it !

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (5):
            EnableDigitalChannel :          Enable a channel
            DisableDigitalChannel :         Disable a channel
            SetDigitalChannelThreshold :    Configure threshold for a group of channels
            EnableDigital :                 Enable global digital engine
            DisableDigital :                Disable global digital engine

<a id="digital.digital.SiglentDigital.EnableDigitalChannel"></a>

#### EnableDigitalChannel

```python
def EnableDigitalChannel(Channel: SiglentDChannel)
```

pySDS [Digital][EnableDigitalChannel] : Enable a digital channel and display it on the screen

    Arguments :
        Channel : SiglentDChannel to be enabled and shown

    Returns :
        self.GetAllErrors()

<a id="digital.digital.SiglentDigital.DisableDigitalChannel"></a>

#### DisableDigitalChannel

```python
def DisableDigitalChannel(Channel: SiglentDChannel)
```

pySDS [Digital][DisableDigitalChannel] : Disable a digital channel and display it on the screen

    Arguments :
        Channel : SiglentDChannel to be disabled and hide

    Returns :
        self.GetAllErrors()

<a id="digital.digital.SiglentDigital.SetDigitalChannelThreshold"></a>

#### SetDigitalChannelThreshold

```python
def SetDigitalChannelThreshold(Group: int, Threshold, Value=0)
```

pySDS [Digital][SetDigitalChannelThreshold] : Configure the threshold for a type of logic signals.

WARNING : This setting is applied for a group of 8 channels. There is only two groups.

    Arguments :
        Group : 1 | 2 Group where the setting is applied
        Threshold : TTL | CMOS | CMOS3.3 | CMOS2.5 | CUSTOM
        Value : Only for CUSTOM, the value in V between -5 and 5

    Returns :
        self.GetAllErrors() : List of errors
        or
        Errors codes

    Errors codes :
        -1 : Invalid group
        -2 : Invalid Threshold type
        -3 : Invalid value

<a id="digital.digital.SiglentDigital.EnableDigital"></a>

#### EnableDigital

```python
def EnableDigital()
```

pySDS [Digital][EnableDigital] : Enable the digital section on the scope

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="digital.digital.SiglentDigital.DisableDigital"></a>

#### DisableDigital

```python
def DisableDigital()
```

pySDS [Digital][DisableDigital] : Disable the digital section on the scope

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="digital.digitalchannel"></a>

# digital.digitalchannel

<a id="digital.digitalchannel.SiglentDChannel"></a>

## SiglentDChannel Objects

```python
class SiglentDChannel(SiglentBase)
```

<a id="digital.digitalchannel.SiglentDChannel.__init__"></a>

#### \_\_init\_\_

```python
def __init__(instr, baseclass, channel)
```

Overhide the standard class init to store some more advanced data !

Check SiglentBase doc before !

Added attributes :
    Private (1) :
        __channel__ :   Descriptor of the channel

    Public (0) :
        None

Added methods :
    Private (0) :
        None

    Public (0) :
        None

