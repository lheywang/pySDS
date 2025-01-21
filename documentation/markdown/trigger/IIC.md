<a id="IIC"></a>

# IIC

<a id="IIC.SiglentIIC"></a>

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

<a id="IIC.SiglentIIC.SetTriggerOnSCL"></a>

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

<a id="IIC.SiglentIIC.SetTriggerOnSDA"></a>

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

<a id="IIC.SiglentIIC.SetTriggerOnCondition"></a>

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

<a id="IIC.SiglentIIC.ConfigureTriggerAddress"></a>

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

<a id="IIC.SiglentIIC.ConfigureTriggerData1"></a>

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

<a id="IIC.SiglentIIC.ConfigureTriggerData2"></a>

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

<a id="IIC.SiglentIIC.ConfigureTriggerQual"></a>

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

<a id="IIC.SiglentIIC.ConfigureTriggerRW"></a>

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

<a id="IIC.SiglentIIC.ConfigureTriggerAddressLen"></a>

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

<a id="IIC.SiglentIIC.ConfigureTriggerDataLen"></a>

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

