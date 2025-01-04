<a id="deprecated_functions"></a>

# deprecated\_functions

<a id="deprecated_functions.acal"></a>

# deprecated\_functions.acal

<a id="deprecated_functions.acal.ACAL"></a>

## ACAL Objects

```python
class ACAL(SiglentBase)
```

<a id="deprecated_functions.acal.ACAL.EnableAutomaticCalibration"></a>

#### EnableAutomaticCalibration

```python
def EnableAutomaticCalibration()
```

PySDS [EnableAutomaticCalibration] :    Enable automatic calibration of the device. (When ? )

WARNING : This command is only available on some CFL series devices

    Arguments :
        None

    Returns :
        self.GetAllErrors() : List of errors

<a id="deprecated_functions.acal.ACAL.DisableAutomaticCalibration"></a>

#### DisableAutomaticCalibration

```python
def DisableAutomaticCalibration()
```

PySDS [DisableAutomaticCalibration] :    Disable automatic calibration of the device.

WARNING : This command is only available on some CFL series devices

    Arguments :
        None

    Returns :
        self.GetAllErrors() : List of errors

<a id="deprecated_functions.acal.ACAL.GetAutomaticCalibrationState"></a>

#### GetAutomaticCalibrationState

```python
def GetAutomaticCalibrationState()
```

PySDS [GetAutomaticCalibrationState] :   Return the state of the autocalibration

WARNING : This command is only available on some CFL series devices

    Arguments :
        None

    Returns :
        True | False if enabled | Disabled

<a id="deprecated_functions.counter"></a>

# deprecated\_functions.counter

<a id="deprecated_functions.date"></a>

# deprecated\_functions.date

<a id="deprecated_functions.date.DATE"></a>

## DATE Objects

```python
class DATE(SiglentBase)
```

<a id="deprecated_functions.date.DATE.GetDate"></a>

#### GetDate

```python
def GetDate()
```

PySDS [GetDate] :   Read and return the date stored on the oscilloscope RTC

Actually, this function does not work, despite that it's presence is stated on the datasheet.
--> Possible issues :
        Function non implemented ?
        Syntax not OK ?

    Arguments :
        None

    Returns :
        Python Datetime object

<a id="deprecated_functions.date.DATE.SetDate"></a>

#### SetDate

```python
def SetDate(Date: datetime)
```

PySDS [SetDate] :   Set the internal RTC date and time

    Arguments :
        Python Datetime object

    Returns :
        self.GetAllErrors() returns (List of errors)

