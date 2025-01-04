<a id="maths"></a>

# maths

<a id="maths.maths"></a>

# maths.maths

<a id="maths.maths.SiglentMaths"></a>

## SiglentMaths Objects

```python
class SiglentMaths(SiglentBase)
```

pySDS [Files][SiglentMaths] :   Class herited from SiglentBase.
                                Store all command related the control of maths functions.

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (1) :
            __init__ :                  Small overhide to add one variable

        Public (12):
            DefineMathOperation :       Configure math operation
            EnableMathInvert :          Invert the output
            DisableMathInvert :         De-Invert the output
            SetMathVDIV :               Configure VDIV of math channel
            SetMathVerticalPosition :   Set Math position
            SetFFTCenter :              Set FFT Center
            SetFTTDisplayMode :         Set FFT Display mode
            SetFFTVerticalPosition :    Set FFT Position
            SetFFTVerticalScale :       Set FFT Scale
            SetFFTHorizontalScale :     Set FFT Horizontal scale
            SetFFTVerticalUnit :        Set FFT Unit
            SetFFTWindow :              Set FFT Unit

<a id="maths.maths.SiglentMaths.__init__"></a>

#### \_\_init\_\_

```python
def __init__(instr, baseclass, number=0)
```

Small overhide to add a variable to the class.

<a id="maths.maths.SiglentMaths.DefineMathOperation"></a>

#### DefineMathOperation

```python
def DefineMathOperation(Equation)
```

pySDS [Maths][DefineMathOperation] : Configure math operation to do.

    Arguments :
        Equation : Human written operation

    Returns :
        self.GetAllErrors()

<a id="maths.maths.SiglentMaths.EnableMathInvert"></a>

#### EnableMathInvert

```python
def EnableMathInvert()
```

pySDS [Math][EnableMathInvert] : Invert the trace of the math result

    Arguments :
        None

    Returns :
        self.GetAllErrors

<a id="maths.maths.SiglentMaths.DisableMathInvert"></a>

#### DisableMathInvert

```python
def DisableMathInvert()
```

pySDS [Math][EnableMathInvert] : Disable inversion the trace of the math result

    Arguments :
        None

    Returns :
        self.GetAllErrors

<a id="maths.maths.SiglentMaths.SetMathVDIV"></a>

#### SetMathVDIV

```python
def SetMathVDIV(Unit)
```

pySDS [Math][SetMathVDIV] : Configure the vertical scale of the math channel

    Arguments :
        Unit : 500uV | 1mV | 2mV | 5mV | 10mV | 20mV | 50mV | 100mV | 200mV | 500mV | 1V | 2V | 5V | 10V | 20V | 50V | 100V

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid unit

<a id="maths.maths.SiglentMaths.SetMathVerticalPosition"></a>

#### SetMathVerticalPosition

```python
def SetMathVerticalPosition(Offset)
```

pySDS [Math][SetMathVerticalPosition] : Configure the position of the math

    Arguments :
        Offset : Value in uV / mV / V to be offseted on the math signal

    Returns :
        self.GetAllErrors()
        or
        -1 : Out of range value (for this VDIV)

<a id="maths.maths.SiglentMaths.SetFFTCenter"></a>

#### SetFFTCenter

```python
def SetFFTCenter(Value)
```

pySDS [Math][SetFFTCenter] : Configure the FFT Center point

WARNING : It's not possible to check the value here

    Arguments :
        Value in Hz | kHz | MHz

    Returns :
        self.GetAllErrors()

<a id="maths.maths.SiglentMaths.SetFTTDisplayMode"></a>

#### SetFTTDisplayMode

```python
def SetFTTDisplayMode(Mode)
```

pySDS [Math][SetFFTDisplayMode] : Configure the mode of display of the FFT

    Arguments :
        Mode : ON | OFF | EXCLU

    Returns :
        self.GetAllErrors()
        or
        -1 : Value not allowed

<a id="maths.maths.SiglentMaths.SetFFTVerticalPosition"></a>

#### SetFFTVerticalPosition

```python
def SetFFTVerticalPosition(Offset)
```

pySDS [Math][SetFFTVerticalPosition] : Configure the VPOS of the FFT

    Arguments :
        Offset : Value in Volts

    Returns :
        self.GetAllErrors()
        or
        -1 : Out of range value

<a id="maths.maths.SiglentMaths.SetFFTVerticalScale"></a>

#### SetFFTVerticalScale

```python
def SetFFTVerticalScale(Scale)
```

pySDS [Math][SetFFTVerticalScale] : Set the FFT scale

WARNING : Due to the option of two units, some values may be valid but not for this specific mode. VRMS is more restrictive.

    Arguments :
        Scale : Value to be used

    Returns :
        self.GetAllErrors()
        or
        -1 : Out of range value

<a id="maths.maths.SiglentMaths.SetFFTHorizontalScale"></a>

#### SetFFTHorizontalScale

```python
def SetFFTHorizontalScale(Scale)
```

pySDS [Math][SetFFTHorizontalScale] : Set the horizontal division of the FFT trace

WARNING : It's not possible to check the value here

    Arguments :
        Scale : in Hz | kHz | Mhz with unit

    Returns :
        self.GetAllErrors()

<a id="maths.maths.SiglentMaths.SetFFTVerticalUnit"></a>

#### SetFFTVerticalUnit

```python
def SetFFTVerticalUnit(Unit)
```

pySDS [Math][SetFFTVerticalUnit] : Set the FFT unit. This function shall be called first when configuring FFT

    Arguments :
        Unit : VRMS | DBM | DBVRMS

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Unit

<a id="maths.maths.SiglentMaths.SetFFTWindow"></a>

#### SetFFTWindow

```python
def SetFFTWindow(Window)
```

pySDS [Math][SetFFTWindow] : Configure the FFT Window to be used

    Arguments :
        Window : RECT | BLAC | HANN | HAMM | FLATTOP

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Window

Doc from siglent :
    RECT — Rectangle is useful for transient signals, and signals where there are an integral number of cycles in the time record.
    BLAC — Blackman reduces time resolution compared to the rectangular window, but it improves the capacity to detect smaller impulses due to lower secondary lobes (provides minimal spectral leakage).
    HANN — Hanning is useful for frequency resolution and general purpose use. It is good for resolving two frequencies that are close together, or for making frequency measurements.
    HAMM — Hamming.
    FLATTOP — Flattop is the best for making accurate amplitude measurements of frequency peaks

