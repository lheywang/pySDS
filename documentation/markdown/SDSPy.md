<a id="pySDS"></a>

# pySDS

<a id="pySDS.PySDS"></a>

## PySDS Objects

```python
class PySDS()
```

PySDS [class] : Parent class of the PySDS package.
                Handle actually all of basic SCPI commands, and call subclasses for some advanced functionnalities !

    Attributes :
        Private :
            __ip__ :            ip of the device. Used internally to check it's validity.
            __rm__ :            pyvisa ressource manager
            __instr__ :         Handle to the pyvisa object to interract with the device
            __ConfigFile__ :    Configuration file used for the scope.
            __Config__ :        Parsed configuration toml file
            __Generics__ :      SCPIGenerics class. Used for low level interraction with the device.

        Public :
            ** Standard variables **
            DeviceOpenned :     Get a non 0 value if the device was openned correctly. Otherwise, take 0
            model :             Device model, parsed from *IDN command
            SN :                Device SN, parsed from *IDN command
            Firmware :          Device firmware revision, parsed from *IDN command

            ** SCPI Variables **
            Channel :           A list of channel presents on the device. Each is it's own SiglentChannel class.
            Trigger :           A SiglentTrigger class



    Methods :
        Private :

        Public :

    Parents :
        None

    Subclass :
        None

<a id="pySDS.PySDS.__init__"></a>

#### \_\_init\_\_

```python
def __init__(IP: str)
```

PySDS [init] :  Initialize the class.
                Use some configuration file to initialize properly the oscilloscope, and read it's actual state to make sure to fetch the real state
                May take some time since a lot of network requests are done here !

    Arguments :
        IP : A string IP address, version 4 of where the ressource shall be allocated

    Returns :
        None

<a id="pySDS.PySDS.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

PySDS [repr] :  Basic print of the connected device.
                Aimed to the developper, and thus expose more informations than the __str__ function !

    Arguments :
        None

    Returns :
        None

<a id="pySDS.PySDS.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

PySDS [repr] :  Basic print of the connected device.
                Aimed to the user, and thus expose less informations than the __repr__ function !

    Arguments :
        None

    Returns :
        None

<a id="pySDS.PySDS.GetAllStatus"></a>

#### GetAllStatus

```python
def GetAllStatus()
```

PySDS [GetAllStatus] :  Return the status of the STB, ESR, INR, DDR, CMD, EXR and URR Registers.

    Arguments :
        None

    Returns :
        List of integers with the values in order

<a id="pySDS.PySDS.EnableBuzzer"></a>

#### EnableBuzzer

```python
def EnableBuzzer()
```

PySDS [EnableBuzzer] :  Enable the device buzzer

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="pySDS.PySDS.DisableBuzzer"></a>

#### DisableBuzzer

```python
def DisableBuzzer()
```

PySDS [DisableBuzzer] : Disable the device buzzer

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="pySDS.PySDS.GetBuzzerEnablingState"></a>

#### GetBuzzerEnablingState

```python
def GetBuzzerEnablingState()
```

PySDS [GetBuzzerEnablingState] :    Return the buzzer enabling state (ON or OFF)

Arguments :
    None

Returns :
    True | False

<a id="pySDS.PySDS.Calibrate"></a>

#### Calibrate

```python
def Calibrate()
```

PySDS [Calibrate] : Calibrate the device.
                    This is actually the fast one, which does not do a full analog frontend calibration.

WARNING :   Leaving probes and other elements connected may affect the result.
            Make sure to calibrate the device in proper conditions !

Arguments :
    None

Returns :
    Integer : If 0, then calibration was sucessfull.

<a id="pySDS.PySDS.Autoset"></a>

#### Autoset

```python
def Autoset()
```

pySDS [Autoset] : Launch an autoset procedure

WARNING :   This should be avoided as possible, since the autoset isn't the most reliable thing in the world.
            It's possible that the scope will show a detail of the waweform where there is some others things to be seen.
            Use in a maximal number of case the manual settings to precisely control the predicted signal

    Arguments :
        None

    Returns :
        self.GetAllErrors() : List of errors that occured

<a id="pySDS.PySDS.LockDevicePanel"></a>

#### LockDevicePanel

```python
def LockDevicePanel()
```

PySDS [LockDevicePanel] : Lock the device front panel to prevent any actions of the user

WARNING : This command seems to exhibit some weird response and no action at all on an SDS824X-HD

    Arguments :
        None

    Returns :
        self.GetAllErrors() : List of errors

<a id="pySDS.PySDS.UnlockDevicePanel"></a>

#### UnlockDevicePanel

```python
def UnlockDevicePanel()
```

PySDS [UnlockDevicePanel] : Unlock the device front panel to enable any actions of the user

WARNING : This command seems to exhibit some weird response and no action at all on an SDS824X-HD

    Arguments :
        None

    Returns :
        self.GetAllErrors() : List of errors

<a id="pySDS.PySDS.GetDevicePanelLockState"></a>

#### GetDevicePanelLockState

```python
def GetDevicePanelLockState()
```

PySDS [GetDevicePanelLockState] : Return the status of the lock on the front panel

WARNING : This command seems to exhibit some weird response and no action at all on an SDS824X-HD

    Arguments :
        None

    Returns :
        Boolean : Lock (True) or not (False)

<a id="pySDS.PySDS.RecallPreset"></a>

#### RecallPreset

```python
def RecallPreset(PresetNumber: int)
```

PySDS [RecallPreset] :  Apply a previously stored list of settings on the device.
                        Can only be called after the call of SavePreset function !
                        If 0 is passed, this is the default config.

    Argument :
        PresentNumber : Integer of the position to store the preset

    Returns :
        self.GetAllErrors() returns (List of errors)
        or
        -1 : Invalid preset ID

<a id="pySDS.PySDS.SavePresent"></a>

#### SavePresent

```python
def SavePresent(PresetNumber: int)
```

PySDS [SavePresent] :   Store the settings of the device into a defined non volatile memory location.
                        Number 0 is not valid, since this location is the default preset.

    Argument :
        PresentNumber : Integer of the position to store the preset

    Returns :
        self.GetAllErrors() returns (List of errors)
        or
        -1 : Invalid preset ID

<a id="pySDS.PySDS.ResetDevice"></a>

#### ResetDevice

```python
def ResetDevice()
```

PySDS [ResetDevice] : Perform a software reset of the device

Arguments :
    None

Returns :
    self.GetAllErrors() returns (List of errors)

<a id="pySDS.PySDS.GetAllErrors"></a>

#### GetAllErrors

```python
def GetAllErrors(print=False)
```

PySDS [GetAllErrors] :  Read the device errors, and until at least one error exist, continue to read it.
                        For each errors, it will be printed in console and returned on a list, with it's lengh in first position.

                        This function also trigger a reading of the status of the device to detect if value where adapted or cancelled.

    Arguments :
        print : Shall we print the decoded output on the console ? Default to false.

    Returns :
        List :
            Index 0 :       Number of errors that occured
            Index 1 - n :   Device errors codes

<a id="pySDS.PySDS.GetDeviceStatus"></a>

#### GetDeviceStatus

```python
def GetDeviceStatus(print=False)
```

PySDS [GetDeviceStatus] :   Get the device status, and parse it to make it easier to use for developpers or users.
                            Print each status bit

    Argument :
        print : Shall we print the decoded output on the console ? Default to false.

    Returns :
        List of lenght 16, for each bit

<a id="pySDS.PySDS.GetDeviceOptions"></a>

#### GetDeviceOptions

```python
def GetDeviceOptions()
```

PySDS [GetDeviceOptions] :  Return the list of the installed device options.
                            Function isn't working for now, but the response seems correct.
                            --> Return 0 where it shall return OPC 0...

    Arguments :
        None

    Returns :
        List of String for all options

<a id="pySDS.PySDS.GetDeviceStatus"></a>

#### GetDeviceStatus

```python
def GetDeviceStatus()
```

PySDS [GetDeviceStatus] :   Read the device status, and parse it to be easier for the user to read !

    Arguments :
        None

    Returns :
        List of lenght 16, for each bit

