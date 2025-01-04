<a id="history"></a>

# history

<a id="history.history"></a>

# history.history

<a id="history.history.SiglentHistory"></a>

## SiglentHistory Objects

```python
class SiglentHistory(SiglentBase)
```

pySDS [History][SiglentHistory] :   Class herited from SiglentBase.
                                    Store all command related the control of history display.

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (7):
            EnableHistory :                 Enable history mode
            DisableHistory :                Disable history mode
            SetCurrentFrame :               Configure current frame
            GetFrameAcquisitionTime :       GetAcquisitionTime for a defined frame
            EnableHistoryList :             Enable List view
            DisableHistoryList :            Disable List view

<a id="history.history.SiglentHistory.EnableHistory"></a>

#### EnableHistory

```python
def EnableHistory()
```

pySDS [History][EnableHistory] : Enable the History mode

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="history.history.SiglentHistory.DisableHistory"></a>

#### DisableHistory

```python
def DisableHistory()
```

pySDS [History][DisableHistory] : Disable the History mode

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="history.history.SiglentHistory.SetCurrentFrame"></a>

#### SetCurrentFrame

```python
def SetCurrentFrame(Number)
```

pySDS [History][SetCurrentFrame] : Configure the current frame where the data is stored

    Arguments :
        Number : Integer of the position. Generally between 0 and 7960, but upper value can be influed by hardware options, timebase or resolution.

    Returns :
        self.GetAllErrors() : List of errors

<a id="history.history.SiglentHistory.GetFrameAcquisitionTime"></a>

#### GetFrameAcquisitionTime

```python
def GetFrameAcquisitionTime()
```

pySDS [History][GetFrameAcquisitionTime] : Return the acquision time for this frame

    Arguments :
        None

    Returns :
        Duration under the form of a Python Time object (from Datetime package)

<a id="history.history.SiglentHistory.EnableHistoryList"></a>

#### EnableHistoryList

```python
def EnableHistoryList()
```

pySDS [History][EnableHistoryList] : Enable the list mode

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="history.history.SiglentHistory.DisableHistoryList"></a>

#### DisableHistoryList

```python
def DisableHistoryList()
```

pySDS [History][DisableHistoryList] : Disable the list mode

    Arguments :
        None

    Returns :
        self.GetAllErrors()

