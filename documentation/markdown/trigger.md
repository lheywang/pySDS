<a id="trigger"></a>

# trigger

<a id="trigger.CAN"></a>

# trigger.CAN

<a id="trigger.CAN.SiglentCAN"></a>

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

<a id="trigger.CAN.SiglentCAN.SetTriggerOnCANH"></a>

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

<a id="trigger.CAN.SiglentCAN.SetTriggerOnCondition"></a>

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

<a id="trigger.CAN.SiglentCAN.ConfigureTriggerID"></a>

#### ConfigureTriggerID

```python
def ConfigureTriggerID(ID: int)
```

pySDS [CAN][ConfigureTriggerID] : Set the ID for ID and ID_AND_DATA mode of trigger

    Arguments :
        ID : Integer between 0-2048 (11 bits) or 0-536870912 (29 bits)

    Returns :
        self.GetAllErrors()

<a id="trigger.CAN.SiglentCAN.ConfigureTriggerIDLen"></a>

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

<a id="trigger.CAN.SiglentCAN.ConfigureTriggerData1"></a>

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

<a id="trigger.CAN.SiglentCAN.ConfigureTriggerData2"></a>

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

<a id="trigger.CAN.SiglentCAN.SetTriggerBaud"></a>

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

<a id="trigger.IIC"></a>

# trigger.IIC

<a id="trigger.IIC.SiglentIIC"></a>

## SiglentIIC Objects

```python
class SiglentIIC(SiglentBase)
```

pySDS [Trigger][SiglentIIC] :   Class herited from SiglentBase.
                                Store all command related the control of the triggering system for the I2C bus

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (10):
            SetTriggerOnSCL :               Set the trigger on the SCL Bus
            SetTriggerOnSDA :               Set the trigger on the SDA Bus
            SetTriggerOnCondition :         Set the trigger on advanced conditions
            ConfigureTriggerAddress :       Set the trigger address condition
            ConfigureTriggerData1 :         Set the trigger data 1 condition
            ConfigureTriggerData2 :         Set the trigger data 2 condition
            ConfigureTriggerQual :          Set the trigger eeprom qualifier condition
            ConfigureTriggerRW :            Set the read / write condition
            ConfigureTriggerAddressLen :    Set the address len condition
            ConfigureTriggerDataLen :       Set the data len condition

<a id="trigger.IIC.SiglentIIC.SetTriggerOnSCL"></a>

#### SetTriggerOnSCL

```python
def SetTriggerOnSCL(Channel, Threshold=1.65)
```

pySDS [IIC][SetTriggerOnSCL] : Configure the trigger on the SCL bus.

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the SCL pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="trigger.IIC.SiglentIIC.SetTriggerOnSDA"></a>

#### SetTriggerOnSDA

```python
def SetTriggerOnSDA(Channel, Threshold=1.65)
```

pySDS [IIC][SetTriggerOnSDA] : Configure the trigger on the SDA bus.

    Arguments :
        Channel :       SiglentChannel or SiglentDCHannel related to the SDA pin
        Threshold :     For analog channel only, the used voltage. Default to 1.65

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Channel

<a id="trigger.IIC.SiglentIIC.SetTriggerOnCondition"></a>

#### SetTriggerOnCondition

```python
def SetTriggerOnCondition(Condition: str)
```

pySDS [IIC][SetTriggerOnCondition] : Set the trigger on a bus transfer condition

WARNING : Once the condition is selected, further configuration may be needed.

    Arguments :
        Condition : The selected condition

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid condition

    Possibles conditions :
        START : Start condition.
        STOP : Stop condition.
        RESTART : Another start condition occurs before a stop condition.
        NOACK : Missing acknowledge.
        EEPROM : EEPROM frame containing (Start:Controlbyte:R:Ack:Data).
        7ADDA : 7-bit address frame containing (Start:Address7:R/W:Ack:Data:Data2).
        10ADDA : 10-bit address frame containing (Start:Address10:R/W:Ack:Data:Data2).
        DALENTH : specifie a search based on address lengthand data length.

<a id="trigger.IIC.SiglentIIC.ConfigureTriggerAddress"></a>

#### ConfigureTriggerAddress

```python
def ConfigureTriggerAddress(Address: int)
```

pySDS [IIC][ConfigureTriggerAddress] : Set the trigger on a specific address on the bus (7ADDA or 10ADDA only)

WARNING : A condition must be configured to access to this function

    Arguments :
        Address : The device address, 0-128 or 0-1024 (7 or 10 bit address). Address is casted to integer prior device write.

    Returns :
        self.GetAllErrors()

<a id="trigger.IIC.SiglentIIC.ConfigureTriggerData1"></a>

#### ConfigureTriggerData1

```python
def ConfigureTriggerData1(Data: int)
```

pySDS [IIC][ConfigureTriggerData1] : Set the first byte of data on the bus to be filtered (7ADDA or 10ADDA only)

WARNING : A condition must be configured to access to this function

    Arguments :
        Data : The data, 0-256. Data is casted to integer prior device write.

    Returns :
        self.GetAllErrors()

<a id="trigger.IIC.SiglentIIC.ConfigureTriggerData2"></a>

#### ConfigureTriggerData2

```python
def ConfigureTriggerData2(Data: str)
```

pySDS [IIC][ConfigureTriggerData2] : Set the second byte of data on the bus to be filtered (7ADDA or 10ADDA only)

WARNING : A condition must be configured to access to this function

    Arguments :
        Data : The data, 0-256. Data is casted to integer prior device write.

    Returns :
        self.GetAllErrors()

<a id="trigger.IIC.SiglentIIC.ConfigureTriggerQual"></a>

#### ConfigureTriggerQual

```python
def ConfigureTriggerQual(Qual: str)
```

pySDS [IIC][ConfigureTriggerQual] : Configure the qualifier on the bus (EEPROM mode only)

WARNING : A condition  must be configured to access to this function

    Arguments :
        Qaulifier : EQUAL | MORE | LESS

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid qualifier

<a id="trigger.IIC.SiglentIIC.ConfigureTriggerRW"></a>

#### ConfigureTriggerRW

```python
def ConfigureTriggerRW(RW: str)
```

pySDS [IIC][ConfigureTriggerRW]: Configure the trigger to detect read or write operations

WARNING : A condition must be configured to access to this function

    Arguments :
        RW : READ | WRITE | DONT_CARE

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid RW

<a id="trigger.IIC.SiglentIIC.ConfigureTriggerAddressLen"></a>

#### ConfigureTriggerAddressLen

```python
def ConfigureTriggerAddressLen(Addr: str)
```

pySDS [IIC][ConfigureTriggerAddressLen] : Configure the size of the address to be waited. (Data Len mode only)

WARNING : A condition must be configured to access to this function

    Arguments :
        Addr : 7BIT | 10BIT

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Address len

<a id="trigger.IIC.SiglentIIC.ConfigureTriggerDataLen"></a>

#### ConfigureTriggerDataLen

```python
def ConfigureTriggerDataLen(Len: int)
```

pySDS [IIC][ConfigureTriggerDataLen] : Configure the number of byte in the message to trigger. (Data Len mode only)

WARNING : A condition must be configured to access to this function

    Arguments :
        Len : Integer, between 1 and 12

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Len

<a id="trigger.LIN"></a>

# trigger.LIN

<a id="trigger.LIN.SiglentLIN"></a>

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

<a id="trigger.LIN.SiglentLIN.SetTriggerOnSRC"></a>

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

<a id="trigger.LIN.SiglentLIN.SetTriggerOnCondition"></a>

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

<a id="trigger.LIN.SiglentLIN.ConfigureTriggerID"></a>

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

<a id="trigger.LIN.SiglentLIN.ConfigureTriggerData1"></a>

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

<a id="trigger.LIN.SiglentLIN.ConfigureTriggerData2"></a>

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

<a id="trigger.LIN.SiglentLIN.SetTriggerBaud"></a>

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

<a id="trigger.SPI"></a>

# trigger.SPI

<a id="trigger.SPI.SiglentSPI"></a>

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

<a id="trigger.SPI.SiglentSPI.SetTriggerOnCLK"></a>

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

<a id="trigger.SPI.SiglentSPI.SetTriggerClockEdge"></a>

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

<a id="trigger.SPI.SiglentSPI.SetTriggerClockTimeout"></a>

#### SetTriggerClockTimeout

```python
def SetTriggerClockTimeout(Timeout: str)
```

pySDS [SPI][SetTriggerClockTimeout] : Set the timeout value (related to clock) when the CS is timeout.

    Arguments :
        Timeout : from 100ns to 500ms (no check done)

    Returns :
        self.GetAllErrors()

<a id="trigger.SPI.SiglentSPI.SetTriggerOnMOSI"></a>

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

<a id="trigger.SPI.SiglentSPI.SetTriggerOnMISO"></a>

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

<a id="trigger.SPI.SiglentSPI.SetTriggerCSType"></a>

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

<a id="trigger.SPI.SiglentSPI.SetTriggerOnCS"></a>

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

<a id="trigger.SPI.SiglentSPI.SetTriggerOnNCS"></a>

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

<a id="trigger.SPI.SiglentSPI.ConfigureTriggerSource"></a>

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

<a id="trigger.SPI.SiglentSPI.ConfigureTriggerDataSequence"></a>

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

<a id="trigger.SPI.SiglentSPI.ConfigureTriggerDataLen"></a>

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

<a id="trigger.SPI.SiglentSPI.SetTriggerBitOrder"></a>

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

<a id="trigger.trigger"></a>

# trigger.trigger

<a id="trigger.trigger.SiglentTrigger"></a>

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

<a id="trigger.trigger.SiglentTrigger.__init__"></a>

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

<a id="trigger.trigger.SiglentTrigger.SetCoupling"></a>

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

<a id="trigger.trigger.SiglentTrigger.SetDelay"></a>

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

<a id="trigger.trigger.SiglentTrigger.GetDelay"></a>

#### GetDelay

```python
def GetDelay()
```

PySDS [Trigger][GetDelay] :  Read the delay applied between trigger and acquisition

    Arguments :
        None

    Returns :
        Float : The number of ms of delay

<a id="trigger.trigger.SiglentTrigger.SetLevel1"></a>

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

<a id="trigger.trigger.SiglentTrigger.SetLevel2"></a>

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

<a id="trigger.trigger.SiglentTrigger.SetMode"></a>

#### SetMode

```python
def SetMode(Mode)
```

PySDS [Trigger][SetMode] :  Configure the mode of operation of the trigger

    Arguments :
        Mode : AUTO | NORM | SINGLE | STOP : Restrained to theses values by an enum.

    Returns :
        Float : The number of ms of delay

<a id="trigger.trigger.SiglentTrigger.GetMode"></a>

#### GetMode

```python
def GetMode()
```

PySDS [Trigger][GetMode] :  Read the mode of operation of the trigger

    Arguments :
        None

    Returns :
        String : The mode

<a id="trigger.trigger.SiglentTrigger.SetSelect"></a>

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

<a id="trigger.trigger.SiglentTrigger.GetSelect"></a>

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

<a id="trigger.trigger.SiglentTrigger.SetSlope"></a>

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

<a id="trigger.trigger.SiglentTrigger.GetSlope"></a>

#### GetSlope

```python
def GetSlope(Channel)
```

PySDS [Trigger][GetSlope] :  Return the configured slope for the trigger

    Arguments :
        Channel : The channel used for trigger. (Warning : Make sure to remain consistent, otherwise the last channel used will be used)

    Returns :
        String : The slope used

<a id="trigger.trigger.SiglentTrigger.SetWindow"></a>

#### SetWindow

```python
def SetWindow(Value: float)
```

PySDS [Trigger][SetWindow] :  Set the height of the Window used for trigger

    Arguments :
        Value (float) : The value in volt

    Returns :
        self.GetAllErrors() : List of errors

<a id="trigger.trigger.SiglentTrigger.GetWindow"></a>

#### GetWindow

```python
def GetWindow()
```

PySDS [Trigger][GetWindow] :  Get the height of the trigger window

    Arguments :
        None

    Returns :
        Value in volt (float)

<a id="trigger.trigger.SiglentTrigger.SetPattern"></a>

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

<a id="trigger.trigger.SiglentTrigger.GetPattern"></a>

#### GetPattern

```python
def GetPattern()
```

PySDS [Trigger][GetPattern] : Read the used pattern trigger

    Arguments :
        None

    Returns :
        List of Channel, Conditions and Pattern

<a id="trigger.UART"></a>

# trigger.UART

<a id="trigger.UART.SiglentUART"></a>

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

<a id="trigger.UART.SiglentUART.SetTriggerOnRX"></a>

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

<a id="trigger.UART.SiglentUART.SetTriggerOnTX"></a>

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

<a id="trigger.UART.SiglentUART.SetTriggerDataSource"></a>

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

<a id="trigger.UART.SiglentUART.SetTriggerCondition"></a>

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

<a id="trigger.UART.SiglentUART.SetTriggerQualifier"></a>

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

<a id="trigger.UART.SiglentUART.ConfigureTriggerData"></a>

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

<a id="trigger.UART.SiglentUART.SetTriggerBaud"></a>

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

<a id="trigger.UART.SiglentUART.ConfigureTriggerDataLen"></a>

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

<a id="trigger.UART.SiglentUART.ConfigureTriggerParity"></a>

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

<a id="trigger.UART.SiglentUART.ConfigureTriggerPolarity"></a>

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

<a id="trigger.UART.SiglentUART.ConfigureTriggerStop"></a>

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

<a id="trigger.UART.SiglentUART.ConfigureTriggerBitOrder"></a>

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

