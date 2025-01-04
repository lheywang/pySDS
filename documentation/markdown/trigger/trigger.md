<a id="trigger"></a>

# trigger

<a id="trigger.SiglentTrigger"></a>

## SiglentTrigger Objects

```python
class SiglentTrigger(SiglentBase)
```

pySDS [Files][SiglentTrigger] : Class herited from SiglentBase.
                                Store all command related the control of the triggering system

                                Due to advanced features available, this class group subclasses.
                                Thus, it's possible to trigger on serial busses for a specific address or conditions.

WARNING : Advanced features are linked to bus decoding ability, and can sometimes interfer between their configurations !

    Attributes :
        Herited from SiglentBase
        +
        I2C (SiglentIIC Class), specified for I2C operation
        SPI (SiglentSPI Class), specified for SPI operation
        LIN (SiglentLIN Class), specified for LIN operation
        SERIAL (SiglentUART Class), specified for UART operation
        CAN (SiglentCAN Class), specified for CAN Operation

    Methods :
        Private (0) :
            None

        Public (15):
            SetCoupling :   Configure trigger coupling
            SetDelay :      Configure trigger delay
            GetDelay :      Get trigger delay
            SetLevel1 :     Set threshold 1
            SetLevel2 :     Set threshold 2
            SetMode :       Set trigger mode
            GetMode :       Get trigger mode
            SetSelect :     Set select
            GetSelect :     Get trigger select
            SetSlope :      Set trigger slope
            GetSlope :      Get trigger slope
            SetWindow :     Set trigger Window
            GetWindow :     Get trigger Window
            SetPattern :    Set trigger pattern
            GetPattern :    Get trigger pattern

<a id="trigger.SiglentTrigger.__init__"></a>

#### \_\_init\_\_

```python
def __init__(instr, baseclass, number=0)
```

Overhide the standard class init to store some more advanced data !

Check SiglentBase doc before !

Added attributes :
    Private (0) :

    Public (0) :
        I2C (SiglentIIC Class), specified for I2C operation
        SPI (SiglentSPI Class), specified for SPI operation
        LIN (SiglentLIN Class), specified for LIN operation
        SERIAL (SiglentUART Class), specified for UART operation
        CAN (SiglentCAN Class), specified for CAN Operation

Added methods :
    Private (0) :
        None

    Public (0) :
        None

<a id="trigger.SiglentTrigger.SetCoupling"></a>

#### SetCoupling

```python
def SetCoupling(Channel, Mode)
```

PySDS [Trigger][SetCoupling] :  Configure the source and coupling of the trigger

WARNING : The command to know the state of the trigger hasn't been developped since it suppose we know the channel used...

    Arguments :
        Channel : C1 | C2 | C3 | C4 | EX | EX5 | LINE : You can pass a member of the ENUM TriggerSources, or it's string. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
        Mode : AC | DC | HFREF | LFREJ : You can pass a member of the ENUM TriggerModes or it's name direcly

    Returns :
        self.GetAllErrors() : List of errors

<a id="trigger.SiglentTrigger.SetDelay"></a>

#### SetDelay

```python
def SetDelay(Delay: float)
```

PySDS [Trigger][SetDelay] :  Configure the delay (may be positive or negatives)* between the trigger and the first acquistion

WARNING : Positive delay are only supported on some devices.

    Arguments :
        Delay : The delay in ms to apply

    Returns :
        self.GetAllErrors() : List of errors

<a id="trigger.SiglentTrigger.GetDelay"></a>

#### GetDelay

```python
def GetDelay()
```

PySDS [Trigger][GetDelay] :  Read the delay applied between trigger and acquisition

    Arguments :
        None

    Returns :
        Float : The number of ms of delay

<a id="trigger.SiglentTrigger.SetLevel1"></a>

#### SetLevel1

```python
def SetLevel1(Channel, Value: float)
```

PySDS [Trigger][SetLevel1] :  Set the level of the specified trigger for a specific channel

    Arguments :
        Channel : C1 | C2 | C3 | C4 | EX | EX5 | LINE : You can pass a member of the ENUM TriggerSources, or it's string. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
        Value : The value in V where to place the trigger

    Returns :
        self.GetAllErrors() : List of errors

<a id="trigger.SiglentTrigger.SetLevel2"></a>

#### SetLevel2

```python
def SetLevel2(Channel, Value: float)
```

PySDS [Trigger][SetLevel2] :  Set the level of the specified trigger for a specific channel

WARNING : This function is not available on SPO devices

    Arguments :
        Channel : C1 | C2 | C3 | C4 | EX | EX5 | LINE : You can pass a member of the ENUM TriggerSources, or it's string. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
        Value : The value in V where to place the trigger

    Returns :
        self.GetAllErrors() : List of errors

<a id="trigger.SiglentTrigger.SetMode"></a>

#### SetMode

```python
def SetMode(Mode)
```

PySDS [Trigger][SetMode] :  Configure the mode of operation of the trigger

    Arguments :
        Mode : AUTO | NORM | SINGLE | STOP : Restrained to theses values by an enum.

    Returns :
        Float : The number of ms of delay

<a id="trigger.SiglentTrigger.GetMode"></a>

#### GetMode

```python
def GetMode()
```

PySDS [Trigger][GetMode] :  Read the mode of operation of the trigger

    Arguments :
        None

    Returns :
        String : The mode

<a id="trigger.SiglentTrigger.SetSelect"></a>

#### SetSelect

```python
def SetSelect(*args)
```

PySDS [Trigger][SetSelect] :  Configure the trigger for very advanced usages.

WARNING :   Due to the very advanced usage of this function, and the poor traduction / updates of the documentation, I'm currently unable to provide checking.
            Thus, the function will only pass settings as given, without even trying to make a compatibility check.

    Arguments :
        None

    Returns :
        self.GetAllErrors() : List of errors

<a id="trigger.SiglentTrigger.GetSelect"></a>

#### GetSelect

```python
def GetSelect()
```

PySDS [Trigger][GetSelect] :    Read the trigger select configuration

WARNING : Due to the complexity of this function, and the lack of proper traduction / explanations, this function only return a string.

    Arguments :
        None

    Returns :
        String :Command output

<a id="trigger.SiglentTrigger.SetSlope"></a>

#### SetSlope

```python
def SetSlope(Channel, Slope)
```

PySDS [Trigger][SetSlope] :  Configure the 'orientation' of the edge used to trigger.

    Arguments :
        Channel : The channel used for trigger. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)
        Slope : NEG | POS | WINDOW : The edge used to trigger

    Returns :
        self.GetAllErrors() : List of errors TRSL

<a id="trigger.SiglentTrigger.GetSlope"></a>

#### GetSlope

```python
def GetSlope(Channel)
```

PySDS [Trigger][GetSlope] :  Return the configured slope for the trigger

    Arguments :
        Channel : The channel used for trigger. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)

    Returns :
        String : The slope used

<a id="trigger.SiglentTrigger.SetWindow"></a>

#### SetWindow

```python
def SetWindow(Value: float)
```

PySDS [Trigger][SetWindow] :  Set the height of the Window used for trigger

    Arguments :
        Value (float) : The value in volt

    Returns :
        self.GetAllErrors() : List of errors

<a id="trigger.SiglentTrigger.GetWindow"></a>

#### GetWindow

```python
def GetWindow()
```

PySDS [Trigger][GetWindow] :  Get the height of the trigger window

    Arguments :
        None

    Returns :
        Value in volt (float)

<a id="trigger.SiglentTrigger.SetPattern"></a>

#### SetPattern

```python
def SetPattern(Sources: list, Status: list, Pattern)
```

PySDS [Trigger][SetPattern] :  Configure a triggering pattern (Enable multi channel triggering)

    Arguments :
        Source : List of the sources used for the operation. Can only be C1 | C2 | C3 | C4
        Status : List of the status for each source : X | L | H (X = don't care)
        Pattern : AND | OR | NAND | NOR

    Returns :
        self.GetAllErrors() : List of errors

<a id="trigger.SiglentTrigger.GetPattern"></a>

#### GetPattern

```python
def GetPattern()
```

PySDS [Trigger][GetPattern] : Read the used pattern trigger

    Arguments :
        None

    Returns :
        List of Channel, Conditions and Pattern

