<a id="decode"></a>

# decode

<a id="decode.decode"></a>

# decode.decode

<a id="decode.decode.SiglentDecode"></a>

## SiglentDecode Objects

```python
class SiglentDecode(SiglentBase)
```

pySDS [Decode][SiglentDecode] : Class herited from SiglentBase.
                                Store all command related the control of digital bus decoding
    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (8):
            EnableDecode :          Enable the bus decoding ability
            DisableDecode :         Disable the bus decoding ability
            ConfigureDecode :       Configure the global bus decoding behavior
            ConfigureI2CDecode :    Configure the I2C Decoding
            ConfigureSPIDecode :    Configure the SPI Decoding
            ConfigureUARTDecode :   Configure the UART Decoding
            ConfigureCANDecode :    Configure the CAN Decoding
            ConfigureLINDecode :    Configure the LIN Decoding

<a id="decode.decode.SiglentDecode.EnableDecode"></a>

#### EnableDecode

```python
def EnableDecode()
```

pySDS [Decode][EnableDecode] : Enable the decode option on the scope

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="decode.decode.SiglentDecode.DisableDecode"></a>

#### DisableDecode

```python
def DisableDecode()
```

pySDS [Decode][DisableDecode] : Disable the decode option on the scope

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="decode.decode.SiglentDecode.ConfigureDecode"></a>

#### ConfigureDecode

```python
def ConfigureDecode(Bus: int,
                    Format="HEX",
                    List="OFF",
                    Link="",
                    Scroll=0,
                    Lines=0)
```

pySDS [Decode][ConfigureDecode] : Configure the decode engine

    Arguments :
        Bus : 1 | 2 (Bus number)
        Format : BIN | DEC | HEX (Mode of print on screen) Default to HEX
        List : OFF | D1 | D2 Default to OFF
        Link : TR_TO_DC | DC_TO_TR
        Scroll : Integer
        Lines : Integer

    Returns :
        GetAllErrors() : List of errors
        or
        [n, Error codes] if errors occured within the function

    Errors codes :
        -1 :    Invalid Lines number
        -2 :    Invalid scroll number (must be > 0 and < Lines)
        -3 :    Invalid Link mode
        -4 :    Invalid List mode
        -5 :    Invalid format
        -6 :    Invalid Bus

<a id="decode.decode.SiglentDecode.ConfigureI2CDecode"></a>

#### ConfigureI2CDecode

```python
def ConfigureI2CDecode(Bus: int,
                       SCL,
                       SDA,
                       SCLT: float = 1.65,
                       SDAT: float = 1.65,
                       Display="ON",
                       RW="ON")
```

pySDS [Decode][ConfigureI2CDecode] : Configure the I2C decoding

WARNING : If digital channel is provided, trigger level will be ignored

    Arguments :
        Bus :       Bus number, as in integer
        SCL :       SCL input. May be SiglentChannel or SiglentDigital class
        SDA :       SCL input. May be SiglentChannel or SiglentDigital class
        SCLT :      Trigger Level for SCL                                           Default to 1.65
        SDAT :      Trigger Level for SCL                                           Default to 1.65
        Display :   ON | OFF Display the bus decoding result                        Default to ON
        RW :        ON | OFF Display the Read/Write bit inside of adress, or not    Default to ON

    Returns :
        GetAllErrors() : List of errors
        or
        List or errors codes within the function

    Errors codes :
        -1 :    Wrong object passed on SCL
        -2 :    Wrong object passed on SDA
        -3 :    Invalid mode for Display
        -4 :    Invalid mode for RW
        -5 :    Invalid bus number

<a id="decode.decode.SiglentDecode.ConfigureSPIDecode"></a>

#### ConfigureSPIDecode

```python
def ConfigureSPIDecode(Bus: int,
                       CLK,
                       MOSI,
                       MISO,
                       CS,
                       CSMode="CS",
                       Edge="RISING",
                       Bit="MSB",
                       Len=8,
                       CLKT=1.65,
                       MOSIT=1.65,
                       MISOT=1.65,
                       CST=1.65,
                       CSTimeout=2,
                       Display="ON")
```

pySDS [Decode][ConfigureSPIDecode] : Configure the decoding of the SPI Bus

WARNING : If a digital channel is provided, it's trigger value will be ignored

    Arguments  :
        Bus :       1 | 2 Bus used to decode
        CLK :       Channel for CLK. May be a channel or a digital channel
        MOSI :      Channel for MOSI. May be a channel or a digital channel
        MISO :      Channel for MISO. May be a channel or a digital channel
        CS :        Channel for CS. May be a channel or a digital channel
        CSMode :    CS | NCS | TIMEOUT Configure the CS operation mode                                          Defaults to CS
        Edge :      RISING | FALLING Configure the mode of SPI between mode 0, 2 : Falling or 1, 3 : Rising     Defaults to RISING
        Bit :       MSB | LSB Configure the bit order                                                           Defaults to MSB
        Len :       Configure the transfer length                                                               Defaults to 8 bit
        CLKT :      Configure the trigger level of the CLK.                                                     Defaults to 1.65.
        MOSIT :     Configure the trigger level of the MOSI.                                                    Defaults to 1.65.
        MISOT :     Configure the trigger level of the MISO.                                                    Defaults to 1.65.
        CST :       Configure the trigger level of the CS.                                                      Defaults to 1.65.
        CSTimeout : Timeout value for the CS when in timeout mode                                               Defaults to 2 (us)
        Display :   ON | OFF Display the result on the screen                                                   Defaults to ON

    Returns :
        GetAllErrors() : List of errors
        Or
        List of errors that occured within the function

    Errors codes :
        -1 :    Incorrect type passed for CLK. Waiting for a SiglentChannel or SiglentDChannel
        -2 :    Incorrect type passed for MOSI. Waiting for a SiglentChannel or SiglentDChannel
        -3 :    Incorrect type passed for MISO. Waiting for a SiglentChannel or SiglentDChannel
        -4 :    Incorrect type passed for CS. Waiting for a SiglentChannel or SiglentDChannel
        -5 :    Invalid CS Mode
        -6 :    Invalid Bus
        -7 :    Invalid Edge provided
        -8 :    Invalid bit provided
        -9 :    Len is out of bounds (4-32)
        -10 :   Invalid display mode

<a id="decode.decode.SiglentDecode.ConfigureUARTDecode"></a>

#### ConfigureUARTDecode

```python
def ConfigureUARTDecode(Bus: int,
                        RX,
                        TX,
                        Baud=115200,
                        DLEN=8,
                        Parity="NONE",
                        Stop=1,
                        Polarity="HIGH",
                        Bit="MSB",
                        RXT=1.65,
                        TXT=1.65,
                        Display="ON")
```

pySDS [Decode][ConfigureUARTDecode] : Configure the UART Decoding

WARNING : If a SiglentDChannel is provided, then the associated trigger value will be ignored.

    Arguments :
        Bus :           Select the number of the bus decoder used. 1 | 2
        RX :            SiglentChannel or SiglentDChannel associated with RX
        TX :            SiglentChannel or SiglentDChannel associated with TX
        Baud :          Baud rate.                                              Default to 115200
        DLEN :          Data len.  5 <= Val <= 8                                Default to 8
        Parity :        Parity bit. NONE | EVEN | ODD                           Default to NONE
        Stop :          Number of stop bits. 1 | 1.5 | 2                        Default to 1
        Polarity :      Polarity of the signal. LOW | HIGH                      Default to HIGH
        Bit :           Order of bits on the message. MSB | LSB                 Default to MSB
        RXT :           RX Trigger level.                                       Default to 1.65
        TXT :           TX Trigger level.                                       Default to 1.65
        Dsiplay :       Display the bus or not ON | OFF                         Default to ON

    Returns :
        GetAllErrors() : List of errors
        or
        List of errors that occured within the function execution, presented in the same way.

    Errors codes
        -1 :    Invalid type passed for RX
        -2 :    Invalid type passed for TX
        -3 :    Invalid Parity mode
        -4 :    Invalid stop bit number
        -5 :    Invalid polarity
        -6 :    Invalid bit order
        -7 :    Invalid display mode
        -8 :    Invalid bus number
        -9 :    Invalid data len
        -10 :   Invalid baud rate

<a id="decode.decode.SiglentDecode.ConfigureCANDecode"></a>

#### ConfigureCANDecode

```python
def ConfigureCANDecode(Bus: int,
                       CANH,
                       CANL,
                       SRC,
                       Baud,
                       CANHT=1.65,
                       CANLT=1.65,
                       Display="ON")
```

pySDS [Decode][ConfigureCANDecode] : Configure the CAN decoding operation

WARNING : If a SiglentDChannel is provided, then the associated trigger value will be ignored.

    Arguments :
        Bus :       ID of the bus where to place the decode results
        CANH :      CANH associated SiglentChannel or SiglentDChannel.
        CANL :      CANL associated SiglentChannel or SiglentDChannel.
        SRC :       Source for decoding. CANH_H | CAN_L | SUB_L.
        Baud :      Baud rate of the communication.
        CANHT :     Threshold for the CANH pin.                             Default to 1.65
        CANLT :     Threshold for the CANL pin.                             Default to 1.65
        Display :   Shall we display the decoding on the screen ?           Default to ON

    Returns :
        GetAllErrors() : List of errors
        or
        List of errors that occured within the function execution, formatted in the same way

    Errors codes :
        -1 :    Invalid CANH type passed
        -2 :    Invalid CANL type passed
        -3 :    Invalid SRC
        -4 :    Invalid DISPLAY setting.
        -5 :    Invalid bus ID
        -6 :    Invalid BAUD RATE

<a id="decode.decode.SiglentDecode.ConfigureLINDecode"></a>

#### ConfigureLINDecode

```python
def ConfigureLINDecode(Bus: int, SRC, Baud, SRCT=1.65, Display="ON")
```

pySDS [Decode][ConfigureLINDecode] : Configure the LIn decoding operation

WARNING : If a SiglentDChannel is provided, then the associated trigger value will be ignored.

    Arguments :
        Bus :       ID of the bus where to place the decode results
        SRC :       SiglentChannel or SiglentDChannel associated with the SRC Pin
        Baud :      Baud rate of the communication
        SRCT :      Threshold the SRC Pin.                                              Default to 1.65
        Display :   Shall we show the result on the screen ?                            Default to ON

    Returns :
        GetAllErrors() : List of errors
        or
        List of errors that occured within the function execution, formatted in the same way

    Errors codes :
        -1 :    Invalid SRC type passed
        -2 :    Invalid DISPLAY setting.
        -3 :    Invalid bus ID
        -4 :    Invalid BAUD RATE

