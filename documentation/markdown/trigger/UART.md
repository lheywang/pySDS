<a id="UART"></a>

# UART

<a id="UART.SiglentUART"></a>

## SiglentUART Objects

```python
class SiglentUART(SiglentBase)
```

pySDS [Trigger][SiglentUART] :  Class herited from SiglentBase.
                                Store all command related the control of the triggering system for the UART bus

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (12):
            SetTriggerOnRX :                Set trigger on RX Pin
            SetTriggerOnTX :                Set trigger on TX Pin
            SetTriggerDataSource :          Set used data source
            SetTriggerCondition :           Set trigger condition
            SetTriggerQualifier :           Set trigger qualifier
            ConfigureTriggerData :          Set triggering data
            SetTriggerBaud :                Set triggering baud (act also on bus decoding)
            ConfigureTriggerDataLen :       Set trigger data len (act also on bus decoding)
            ConfigureTriggerParity :        Set trigger parity (act also on bus decoding)
            ConfigureTriggerPolarity :      Set trigger polarity (act also on bus decoding)
            ConfigureTriggerStop :          Set trigger stop bits (act also on bus decoding)
            ConfigureTriggerBitOrder :      Set trigger bit order (act also on bus decoding)

<a id="UART.SiglentUART.SetTriggerOnRX"></a>

#### SetTriggerOnRX

```python
def SetTriggerOnRX(Channel, Threshold=1.65)
```

pySDS [UART][SetTriggerOnRX] : Configure the trigger on the RX pin

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the RX pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="UART.SiglentUART.SetTriggerOnTX"></a>

#### SetTriggerOnTX

```python
def SetTriggerOnTX(Channel, Threshold=1.65)
```

pySDS [UART][SetTriggerOnTX] : Configure the trigger on the TX pin

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the TX pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="UART.SiglentUART.SetTriggerDataSource"></a>

#### SetTriggerDataSource

```python
def SetTriggerDataSource(Source: str)
```

pySDS [UART][SetTriggerDataSource] : Configure the used data source to trigger

    Arguments :
        Source : Data Source used RX | TX

    Returns :
        self.GetAllErrors
        or
        -1 : Invalid Source

<a id="UART.SiglentUART.SetTriggerCondition"></a>

#### SetTriggerCondition

```python
def SetTriggerCondition(Condition)
```

pySDS [UART][SetTriggerCondition] : Set the trigger on a specific case

    Arguments :
        Condition : START | STOP | DATA | ERROR

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Condition

<a id="UART.SiglentUART.SetTriggerQualifier"></a>

#### SetTriggerQualifier

```python
def SetTriggerQualifier(Qualifier)
```

pYSDS [UART][SetTriggerQualifier] : Set the UART Qualifier condition

    Arguments :
        Qualifier : EQUAL | MORE | LESS

    Returns
        self.GetAllErrors()
        or
        -1 : Invalid qualifier

<a id="UART.SiglentUART.ConfigureTriggerData"></a>

#### ConfigureTriggerData

```python
def ConfigureTriggerData(Data)
```

pySDS [UART][ConfigureTriggerData] : Configure triggering data

    Arguments :
        Data : Data to be used

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid value

<a id="UART.SiglentUART.SetTriggerBaud"></a>

#### SetTriggerBaud

```python
def SetTriggerBaud(Baud)
```

pySDS [UART][SetTriggerBaud] : Set the baud rate of the UART comm

    Arguments :
        Baud : Value.

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Baud

<a id="UART.SiglentUART.ConfigureTriggerDataLen"></a>

#### ConfigureTriggerDataLen

```python
def ConfigureTriggerDataLen(Len: int)
```

pySDS [UART][ConfigureTriggerDataLen] : Configure the number of bits to trigger

    Arguments :
        Len : 5 to 8

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Len

<a id="UART.SiglentUART.ConfigureTriggerParity"></a>

#### ConfigureTriggerParity

```python
def ConfigureTriggerParity(Parity: str)
```

pySDS [UART][ConfigureTriggerParity] : Configure the parity bit used

    Arguments :
        Parity : ODD | EVEN | NONE

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Parity

<a id="UART.SiglentUART.ConfigureTriggerPolarity"></a>

#### ConfigureTriggerPolarity

```python
def ConfigureTriggerPolarity(Polarity: str)
```

pySDS [UART][ConfigureTriggerPolarity] : Configure the bus polarity

    Arguments :
        Polarity : LOW | HIGH

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Polarity

<a id="UART.SiglentUART.ConfigureTriggerStop"></a>

#### ConfigureTriggerStop

```python
def ConfigureTriggerStop(Stop: float)
```

pySDS [UART][ConfigureTriggerStop] : Configure the number of stops bits used

    Arguments :
        Stop : 1 | 1.5 | 2

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid stop bit config

<a id="UART.SiglentUART.ConfigureTriggerBitOrder"></a>

#### ConfigureTriggerBitOrder

```python
def ConfigureTriggerBitOrder(Order: str)
```

pySDS [UART][ConfigureTriggerBitOrder] : Configure the bit order on the comm

    Arguments :
        Order : LSB | MSB

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Order

