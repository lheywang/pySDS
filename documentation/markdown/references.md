<a id="references"></a>

# references

<a id="references.references"></a>

# references.references

<a id="references.references.SiglentReference"></a>

## SiglentReference Objects

```python
class SiglentReference(SiglentBase)
```

pySDS [Files][SiglentReference] :   Class herited from SiglentBase.
                                    Store all command related the control of reference channel selection

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (8):
        CloseReference :                Close the reference functions package
        EnableDisplayOfReference :      Enable display
        DisableDisplayOfReference :     Disable display
        SetReferenceLocation :          Set location of the reference (A, B, C, D)
        SetReferenceOffset :            Set reference offset
        SaveWaveformAsReference :       Save waveform as reference
        SetReferenceScale :             Set reference scale
        SetReferenceSource :            Set reference source

<a id="references.references.SiglentReference.CloseReference"></a>

#### CloseReference

```python
def CloseReference()
```

pySDS [Reference][CloseReference] : Close the reference function on the device

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="references.references.SiglentReference.EnableDisplayOfReference"></a>

#### EnableDisplayOfReference

```python
def EnableDisplayOfReference()
```

pySDS [Reference][EnableDisplayOfReference] : Display the used reference on the screen

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="references.references.SiglentReference.DisableDisplayOfReference"></a>

#### DisableDisplayOfReference

```python
def DisableDisplayOfReference()
```

pySDS [Reference][DisableDisplayOfReference] : Hide the used reference on the screen

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="references.references.SiglentReference.SetReferenceLocation"></a>

#### SetReferenceLocation

```python
def SetReferenceLocation(Location)
```

pySDS [Reference][SetReferenceLocation] : Set the location of the actual reference

    Arguments :
        Location : A | B | C | D

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid location

<a id="references.references.SiglentReference.SetReferenceOffset"></a>

#### SetReferenceOffset

```python
def SetReferenceOffset(Offset)
```

pySDS [Reference][SetReferenceOffset] : Apply an offset on the reference display

    Arguments :
        Offset : The offset in volts

    Returns :
        self.GetAllErrors()

<a id="references.references.SiglentReference.SaveWaveformAsReference"></a>

#### SaveWaveformAsReference

```python
def SaveWaveformAsReference()
```

pySDS [Reference][SaveWaveformAsReference] : Save the current channel source on the current reference location

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="references.references.SiglentReference.SetReferenceScale"></a>

#### SetReferenceScale

```python
def SetReferenceScale(Scale)
```

pySDS [Reference][SetReferenceScale] : Set the display reference scale

    Arguments :
        Scale : The unit in volts (500uV - 10V)

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid scale

<a id="references.references.SiglentReference.SetReferenceSource"></a>

#### SetReferenceSource

```python
def SetReferenceSource(Channel: SiglentChannel)
```

pySDS [Reference][SetReferenceSource] : Set the reference channel to be used

    Arguments :
        Channel : SiglentChannel to be used (or MATH)

    Returns :
        self.GetAllErrors()

