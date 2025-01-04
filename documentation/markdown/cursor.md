<a id="cursor"></a>

# cursor

<a id="cursor.cursor"></a>

# cursor.cursor

<a id="cursor.cursor.SiglentCursor"></a>

## SiglentCursor Objects

```python
class SiglentCursor(SiglentBase)
```

pySDS [Cursor][SiglentCursor] : Class herited from SiglentBase.
                                Store all command related the control of cursors
    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (6):
            SetCursorMode :     Set the mode for a cursor
            GetCursorMode :     Read the mode of a cursor
            PlaceCursor :       Place a cursor
            GetPlacedCursor :   Return the placed cursor on a trace
            SetCursorType :     Configure the cursor type
            GetCursorValue :    Read the value of a cursor

<a id="cursor.cursor.SiglentCursor.SetCursorMode"></a>

#### SetCursorMode

```python
def SetCursorMode(Mode)
```

pySDS [Cursor][SetCursorMode] : Set the mode of operation of the cursors

    Arguments :
        Mode :  The mode wanted between OFF | MANUAL | TRACK | (ON)
                *ON is reserved to some legacy devices, it's usage will trigger a warning !

    Returns :
        self.GetAllErrors()
        or
        -1 if invalid mode has been passed

<a id="cursor.cursor.SiglentCursor.GetCursorMode"></a>

#### GetCursorMode

```python
def GetCursorMode()
```

pySDS [Cursor][GetCursorMode] : Return the mode of operation of the cursor

    Arguments :
        None

    Returns :
        Device response

<a id="cursor.cursor.SiglentCursor.PlaceCursor"></a>

#### PlaceCursor

```python
def PlaceCursor(Channel: SiglentChannel, Cursor, Position)
```

pySDS [Cursor][PlaceCursor] : Place a cursor

WARNING :   Each cursor is unique, you can't set twice the cursor on two different channels.
            The device will consider the last call only.

WARNING2 :  Some settings may trigger an out of bound error. Make sure to check the return code of this function.

    Arguments :
        Channel : The channel to which the cursor belong. This is a SiglentChannel class.
        Cursor : VREF | VDIF | TREF | TDIF | HREF | HDIF
        Position : Value where to place the cursor. This value is sensitive to errors and isn't check internally

    Returns :
        GetAllErrors() : Read and return all of the device errors

<a id="cursor.cursor.SiglentCursor.GetPlacedCursor"></a>

#### GetPlacedCursor

```python
def GetPlacedCursor(Channel: SiglentChannel)
```

pySDS [Cursor][GetPlacedCursor] : Return the name of the cursor placed on a channel

    Arguments :
        Channel : The channel to which the cursor belong. This is a SiglentChannel class.

    Returns :
        List of cursor linked to this channel

<a id="cursor.cursor.SiglentCursor.SetCursorType"></a>

#### SetCursorType

```python
def SetCursorType(Type)
```

pySDS [Cursor][SetCursorType] : Configure the cursor type

    Arguments :
        Type : X | -X | Y | -Y

    Returns :
        Configured type
        or "-1" if wrong type passed

<a id="cursor.cursor.SiglentCursor.GetCursorValue"></a>

#### GetCursorValue

```python
def GetCursorValue(Channel: SiglentChannel, Mode)
```

pySDS [Cursor][GetCursorValue] : Return the values of a cursor

WARNING : Make sure that a cursor has been placed on this channel, or the device will trigger an error :

    Arguments :
        Channel : The channel where the measure belong
        Mode : HREL | VREL ==> Read the horizontal or vertical measure

    Returns : (List of values)
        Delta
        (1 / Delta) : Only in HREL mode, 0 in VREL mode
        Value1
        Value2

        or
        [-err, -err, -err, -err] in case or error with err = errror code

    Errors code
        -1 : Error occured while running the command

