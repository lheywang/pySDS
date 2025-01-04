<a id="communication"></a>

# communication

<a id="communication.communication"></a>

# communication.communication

<a id="communication.communication.SiglentCommunication"></a>

## SiglentCommunication Objects

```python
class SiglentCommunication(SiglentBase)
```

pySDS [Communication][SiglentCommunication] :   Class herited from SiglentBase.
                                                Store all command related to the communication bus
    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (2):
            SetCommHeader :      Configure the form of response of the device
            GetCommHeader :      Return the form of response of the device

<a id="communication.communication.SiglentCommunication.SetCommHeader"></a>

#### SetCommHeader

```python
def SetCommHeader(Mode: str)
```

SDSpy [Communication][SetCommHeader] :  Configure the used form to answer for the device.

WARNING :   This function may cause others function to become broken since the parsing from the default answer.
            LONG / SHORT won't cause issues, the real issue is with OFF where the unit is suppressed. Since the parsing remove the last char, you will end up with power errors !

    Arguments :
        Mode : LONG | SHORT | OFF : The mode of response

    Returns :
        self.GetAllErrors() : List of errors

<a id="communication.communication.SiglentCommunication.GetCommHeader"></a>

#### GetCommHeader

```python
def GetCommHeader()
```

SDSpy [Communication][GetCommHeader] :  Return the response form of the device

    Arguments :
        None

    Returns :
        String : The mode of operation

