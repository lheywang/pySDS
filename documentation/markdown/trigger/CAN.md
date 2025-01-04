<a id="CAN"></a>

# CAN

<a id="CAN.SiglentCAN"></a>

## SiglentCAN Objects

```python
class SiglentCAN(SiglentBase)
```

pySDS [Trigger][SiglentCAN] :   Class herited from SiglentBase.
                                Store all command related the control of the triggering system for the CAN bus

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (7):
            SetTriggerOnCANH :          Set trigger Pin.
            SetTriggerOnCondition :     Set trigger on a condition
            ConfigureTriggerID :        Set trigger ID
            ConfigureTriggerIDLen :     Set trigger ID Len
            ConfigureTriggerData1 :     Set trigger first byte
            ConfigureTriggerData2 :     Set trigger second byte
            SetTriggerBaud :            Set trigger baud

<a id="CAN.SiglentCAN.SetTriggerOnCANH"></a>

#### SetTriggerOnCANH

```python
def SetTriggerOnCANH(Channel, Threshold=1.65)
```

pySDS [CAN][SetTriggerOnCANH] : Configure the trigger on the CANH pin

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the CANH pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="CAN.SiglentCAN.SetTriggerOnCondition"></a>

#### SetTriggerOnCondition

```python
def SetTriggerOnCondition(Condition: str)
```

pySDS [CAN][SetTriggerOnCondition] : Configure the trigger on a condition on the CAN Bus

    Arguments :
        Condition : START | REMOTE | ID | ID_AND_DATA | ERROR

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid condition

    Possibles conditions
        START— Start condition.
        REMOTE— Remote frame
        ID— Specifies a search based on ID bits and ID.
        ID_AND_DATA— Specify a search based on ID bits, ID and data.
        ERROR— Error frame

<a id="CAN.SiglentCAN.ConfigureTriggerID"></a>

#### ConfigureTriggerID

```python
def ConfigureTriggerID(ID: int)
```

pySDS [CAN][ConfigureTriggerID] : Set the ID for ID and ID_AND_DATA mode of trigger

    Arguments :
        ID : Integer between 0-2048 (11 bits) or 0-536870912 (29 bits)

    Returns :
        self.GetAllErrors()

<a id="CAN.SiglentCAN.ConfigureTriggerIDLen"></a>

#### ConfigureTriggerIDLen

```python
def ConfigureTriggerIDLen(Len: str)
```

pySDS [CAN][ConfigureTriggerID] : Set the ID len for ID and ID_AND_DATA mode of trigger.

    Arguments :
        Len : 11BITS | 29BITS

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Len

<a id="CAN.SiglentCAN.ConfigureTriggerData1"></a>

#### ConfigureTriggerData1

```python
def ConfigureTriggerData1(Value: int)
```

pySDS [CAN][ConfigureTriggerData1] : Configure the data (first byte) to be used to trigger for ID_AND_DATA mode.

    Arguments :
        Value: 0-255 value

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid value

<a id="CAN.SiglentCAN.ConfigureTriggerData2"></a>

#### ConfigureTriggerData2

```python
def ConfigureTriggerData2(Value: int)
```

pySDS [CAN][ConfigureTriggerData2] : Configure the data (second byte) to be used to trigger for ID_AND_DATA mode.

    Arguments :
        Value: 0-255 value

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid value

<a id="CAN.SiglentCAN.SetTriggerBaud"></a>

#### SetTriggerBaud

```python
def SetTriggerBaud(Baud)
```

pySDS [CAN][SetTriggerBaud] : Set the baud rate of the UART comm

    Arguments :
        Baud : Value. (As a string for standard values, or as an integer for non standard)*

        * Sending a standard as integer will be seen as custom but will also works fine !

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Baud

    Standard baud values :
        5k
        10k
        20k
        50k
        100k
        125k
        250k
        500k
        800k
        1M

