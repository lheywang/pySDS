<a id="SPI"></a>

# SPI

<a id="SPI.SiglentSPI"></a>

## SiglentSPI Objects

```python
class SiglentSPI(SiglentBase)
```

pySDS [Trigger][SiglentSPI] :   Class herited from SiglentBase.
                                Store all command related the control of the triggering system for the SPI bus

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (15):
            SetTriggerOnCLK :                   Set trigger on CLK Pin
            SetTriggerClockEdge :               Set trigger edge (act also on bus decoding)
            SetTriggerClockTimeout :            Set trigger timeout (act also on bus decoding)
            SetTriggerOnMOSI :                  Set trigger on MOSI Pin
            SetTriggerOnMISO :                  Set trigger on MISO Pin
            SetTriggerCSType :                  Set trigger Type (act also on bus decoding)
            SetTriggerOnCS :                    Set trigger on CS Pin
            SetTriggerOnNCS :                   Set trigger on NCS Pin
            ConfigureTriggerSource :            Set trigger Data Source
            ConfigureTriggerDataSequence :      Set trigger data Sequence
            ConfigureTriggerDataLen :           Set trigger Data Len
            SetTriggerBitOrder :                Set trigger bit order (act also on bus decoding)

<a id="SPI.SiglentSPI.SetTriggerOnCLK"></a>

#### SetTriggerOnCLK

```python
def SetTriggerOnCLK(Channel, Threshold=1.65)
```

pySDS [SPI][SetTriggerOnCLK] : Configure the trigger on the SCLK pin.

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the SCLK pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="SPI.SiglentSPI.SetTriggerClockEdge"></a>

#### SetTriggerClockEdge

```python
def SetTriggerClockEdge(Edge: str)
```

pySDS [SPI][SetTriggerClockEdge] : Configure the edge of the clock the data is latched on

    Arguments :
        Edge : RISING | FALLING. The edge used.

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid edge

<a id="SPI.SiglentSPI.SetTriggerClockTimeout"></a>

#### SetTriggerClockTimeout

```python
def SetTriggerClockTimeout(Timeout: str)
```

pySDS [SPI][SetTriggerClockTimeout] : Set the timeout value (related to clock) when the CS is timeout.

    Arguments :
        Timeout : from 100ns to 500ms (no check done)

    Returns :
        self.GetAllErrors()

<a id="SPI.SiglentSPI.SetTriggerOnMOSI"></a>

#### SetTriggerOnMOSI

```python
def SetTriggerOnMOSI(Channel, Threshold=1.65)
```

pySDS [SPI][SetTriggerOnMOSI] : Configure the trigger on the MOSI pin.

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the MOSI pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="SPI.SiglentSPI.SetTriggerOnMISO"></a>

#### SetTriggerOnMISO

```python
def SetTriggerOnMISO(Channel, Threshold=1.65)
```

pySDS [SPI][SetTriggerOnMISO] : Configure the trigger on the MOSI pin

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the MISO pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="SPI.SiglentSPI.SetTriggerCSType"></a>

#### SetTriggerCSType

```python
def SetTriggerCSType(Type: str)
```

pySDS [SPI][SetTriggerCSType] : Set the CS type on the SPI bus

    Arguments :
        Type : CS | NCS | TIMEOUT

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid type

<a id="SPI.SiglentSPI.SetTriggerOnCS"></a>

#### SetTriggerOnCS

```python
def SetTriggerOnCS(Channel, Threshold=1.65)
```

pySDS [SPI][SetTriggerOnMISO] : Configure the trigger on the CS pin

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the CS pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="SPI.SiglentSPI.SetTriggerOnNCS"></a>

#### SetTriggerOnNCS

```python
def SetTriggerOnNCS(Channel, Threshold=1.65)
```

pySDS [SPI][SetTriggerOnMISO] : Configure the trigger on the NCS pin

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the NCS pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="SPI.SiglentSPI.ConfigureTriggerSource"></a>

#### ConfigureTriggerSource

```python
def ConfigureTriggerSource(Source: str)
```

pySDS [SPI][ConfigureTriggerSource] : Configure the trigger source for the SPI

    Arguments :
        Source : MOSI | MISO

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid source

<a id="SPI.SiglentSPI.ConfigureTriggerDataSequence"></a>

#### ConfigureTriggerDataSequence

```python
def ConfigureTriggerDataSequence(Sequence: list)
```

pySDS [SPI][ConfigureTriggerDataSequence] : Configure a matching bit sequence to trigger

    Arguments :
        Sequence : List of char / string : 0 | 1 | X to trigger. Len must match the datalen (not checked)

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid sequence (len not checked)

<a id="SPI.SiglentSPI.ConfigureTriggerDataLen"></a>

#### ConfigureTriggerDataLen

```python
def ConfigureTriggerDataLen(Len: int)
```

pySDS [SPI][ConfigureTriggerDataSequence] : Configure a matching data lenght to trigger

    Arguments :
        Len : 4-96

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Len

<a id="SPI.SiglentSPI.SetTriggerBitOrder"></a>

#### SetTriggerBitOrder

```python
def SetTriggerBitOrder(Order: str)
```

pySDS [SPI][SetTriggerBitOrder] : Set the bit order on the SPI Bus

    Arguments :
        Order : MSB | LSB

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid order

