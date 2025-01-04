<a id="LIN"></a>

# LIN

<a id="LIN.SiglentLIN"></a>

## SiglentLIN Objects

```python
class SiglentLIN(SiglentBase)
```

pySDS [Trigger][SiglentLIN] :   Class herited from SiglentBase.
                                Store all command related the control of the triggering system for the LIN bus

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (15):

<a id="LIN.SiglentLIN.SetTriggerOnSRC"></a>

#### SetTriggerOnSRC

```python
def SetTriggerOnSRC(Channel, Threshold=1.65)
```

pySDS [LIN][SetTriggerOnSRC] : Configure the trigger on the LIN pin

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the LIN pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="LIN.SiglentLIN.SetTriggerOnCondition"></a>

#### SetTriggerOnCondition

```python
def SetTriggerOnCondition(Condition: str)
```

pySDS [LIN][SetTriggerOnCondition] : Configure the trigger on a condition on the CAN Bus

    Arguments :
        Condition : BREAK | DATA_ERROR | ID | ID_AND_DATA

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid condition

    Possibles conditions :
        BREAK— Break condition.
        ID— Specify a search based on ID.
        ID_AND_DATA—Specify a search based on ID and data.
        DATA_ERROR— Error frame.

<a id="LIN.SiglentLIN.ConfigureTriggerID"></a>

#### ConfigureTriggerID

```python
def ConfigureTriggerID(ID: int)
```

pySDS [LIN][ConfigureTriggerID] : Set the ID for ID and ID_AND_DATA mode of trigger

    Arguments :
        ID : Integer between 0-64

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid ID

<a id="LIN.SiglentLIN.ConfigureTriggerData1"></a>

#### ConfigureTriggerData1

```python
def ConfigureTriggerData1(Value: int)
```

pySDS [LIN][ConfigureTriggerData1] : Configure the data (first byte) to be used to trigger for ID_AND_DATA mode.

    Arguments :
        Value: 0-255 value

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid value

<a id="LIN.SiglentLIN.ConfigureTriggerData2"></a>

#### ConfigureTriggerData2

```python
def ConfigureTriggerData2(Value: int)
```

pySDS [LIN][ConfigureTriggerData2] : Configure the data (second byte) to be used to trigger for ID_AND_DATA mode.

    Arguments :
        Value: 0-255 value

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid value

<a id="LIN.SiglentLIN.SetTriggerBaud"></a>

#### SetTriggerBaud

```python
def SetTriggerBaud(Baud)
```

pySDS [LIN][SetTriggerBaud] : Set the baud rate of the UART comm

    Arguments :
        Baud : Value. (As a string for standard values, or as an integer for non standard)*

        * Sending a standard as integer will be seen as custom but will also works fine !

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Baud

    Standard baud values :
        600
        1200
        2400
        4800
        9600
        19200

