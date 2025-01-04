<a id="acquisition"></a>

# acquisition

<a id="acquisition.acquisition"></a>

# acquisition.acquisition

<a id="acquisition.acquisition.SiglentAcquisition"></a>

## SiglentAcquisition Objects

```python
class SiglentAcquisition(SiglentBase)
```

pySDS [Acquision][SiglentAcquisition] :   C lass herited from SiglentBase.
                                            Store all command related to the control of acquision
    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (13):
            Arm :                       Prepare the device to be ready to trigger
            Stop :                      Stop the device to be ready to trigger
            ConfigureAquireMethod :     Configure the way of acquiring data
            SetAverageCount :           Configure the average number of sample
            GetAverageCount :           Get the number of average samples
            GetMemorySize :             Get the size in sample of the memory used
            SetMemorySize :             Configure the size in sample of the memory
            GetAcquisitionStatus :      Return the acquision status
            GetSampleRate :             Return the used sample rate (function of time resolution and channel)
            GetSampleNumber :           Return the number of sample stored
            SetInterpolationMethod :    Configure the interpolation method to be used (only on display, inter points)
            EnableXYMode :              Enable the XY mode
            DisableXYMode :             Disable the XY mode

<a id="acquisition.acquisition.SiglentAcquisition.Arm"></a>

#### Arm

```python
def Arm()
```

pySDS [Acquisition][Arm] : Place the device to be ready to acquire a waveform once a triggering condition has been validated

    Arguments :
        None

    Returns :
        self.GetDeviceStatus()[13] which take 1 if trigger is ready, 0 otherwise

<a id="acquisition.acquisition.SiglentAcquisition.Stop"></a>

#### Stop

```python
def Stop()
```

pySDS [Acquisition][Stop] : Stop the device to be ready to acquire a waveform.

    Arguments :
        None

    Returns :
        self.GetDeviceStatus()[13] which take 1 if trigger is cancelled, 0 otherwise

<a id="acquisition.acquisition.SiglentAcquisition.ConfigureAquireMethod"></a>

#### ConfigureAquireMethod

```python
def ConfigureAquireMethod(Method: str, AverageNumber: int = 1)
```

pySDS [Acquisition][ConfigureAquireMethod] : Configure the way the device handle data acquisition

    Arguments :
        Method : SAMPLING | PEAK_DETECT | AVERAGE | HIGH_RES
        AverageNumber : Number of sample used to compute an average point

    Returns :
        0 | -1 : The device responded with the same settings or differents one.

<a id="acquisition.acquisition.SiglentAcquisition.SetAverageCount"></a>

#### SetAverageCount

```python
def SetAverageCount(AverageNumber)
```

pySDS [Acquisition][SetAverageCount] : Configure the number of sampled used per average

    Arguments :
        AverageNumber : Number of sample used to compute an average point

    Returns :
        self.GetAllErrors()

<a id="acquisition.acquisition.SiglentAcquisition.GetAverageCount"></a>

#### GetAverageCount

```python
def GetAverageCount()
```

pySDS [Acquisition][GetAverageCount] : Return the number of sample used for averaging

    Arguments :
        None

    Returns :
        Integer : Number of samples

<a id="acquisition.acquisition.SiglentAcquisition.GetMemorySize"></a>

#### GetMemorySize

```python
def GetMemorySize()
```

PySDS [Acquisition][GetMemorySize] : Return the number in millions of samples that can be stored into the memory

WARNING : The value is expressed in number of samples, and not in bytes !

    Arguments :
        None

    Returns :
        Integer : The number of **MILLIONS** of sample that can be stored

<a id="acquisition.acquisition.SiglentAcquisition.SetMemorySize"></a>

#### SetMemorySize

```python
def SetMemorySize(value: int)
```

PySDS [Acquisition][SetMemorySize] : Set the memory size for the samples of the scope.

WARNING : The value is expressed in number of samples, and not in bytes !

    Arguments :
        The value in **MILLIONS** to the used.

    Returns :
        self.GetAllErrors() returns (List of errors)

<a id="acquisition.acquisition.SiglentAcquisition.GetAcquisitionStatus"></a>

#### GetAcquisitionStatus

```python
def GetAcquisitionStatus()
```

PySDS [Acquisition][GetAcquisitionStatus] : Return the acquisition status of the device

    Arguments :
        None

    Returns :
        String : Device response

<a id="acquisition.acquisition.SiglentAcquisition.GetSampleRate"></a>

#### GetSampleRate

```python
def GetSampleRate()
```

PySDS [Acquisition][GetSampleRate] : Return the acquisition sample rate that is actually used

    Arguments :
        None

    Returns :
        String : Device response

<a id="acquisition.acquisition.SiglentAcquisition.GetSampleNumber"></a>

#### GetSampleNumber

```python
def GetSampleNumber()
```

PySDS [Acquisition][GetSampleNumber] : Return the acquisition number of points captured

    Arguments :
        None

    Returns :
        String : Device response

<a id="acquisition.acquisition.SiglentAcquisition.SetInterpolationMethod"></a>

#### SetInterpolationMethod

```python
def SetInterpolationMethod(Method)
```

PySDS [Acquisition][SetInterpolationMethod] :   Configure the interpolation method to be used

    Arguments :
        Method : ON | OFF (sine interpolation or linear interpolation)

    Returns :
        self.GetAllErrors()

<a id="acquisition.acquisition.SiglentAcquisition.EnableXYMode"></a>

#### EnableXYMode

```python
def EnableXYMode()
```

PySDS [Acquisition][EnableXYMode] :   Enable the XY mode

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="acquisition.acquisition.SiglentAcquisition.DisableXYMode"></a>

#### DisableXYMode

```python
def DisableXYMode()
```

PySDS [Acquisition][DisableXYMode] :    Disable the XY mode

    Arguments :
        None

    Returns :
        self.GetAllErrors()

