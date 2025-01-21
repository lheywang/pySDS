<a id="timebase"></a>

# timebase

<a id="timebase.timebase"></a>

# timebase.timebase

<a id="timebase.timebase.SiglentTimebase"></a>

## SiglentTimebase Objects

```python
class SiglentTimebase(SiglentBase)
```

pySDS [Files][SiglentTimebase] :    Class herited from SiglentBase.
                                    Store all command related the control of timebase on the display

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (7):

<a id="timebase.timebase.SiglentTimebase.GetTimeDiv"></a>

#### GetTimeDiv

```python
def GetTimeDiv()
```

pySDS [Timebase][GetTimeDiv] : Return the time division used

    Arguments :
        None

    Returns :
        Time division used in seconds

<a id="timebase.timebase.SiglentTimebase.SetTimeDiv"></a>

#### SetTimeDiv

```python
def SetTimeDiv(Timebase: str)
```

pySDS [Timebase][SetTimeDiv] : Configure the timebase used

    Arguments :
        Timebase : Base to be used (from defined list right after)

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid timebase

    Possibles timebases :
        1NS 2NS 5NS
        10NS 20NS 50NS
        100NS 200NS 500NS
        1US 2US 5US
        10US 20US 50US
        100US 200US 500US
        1MS 2MS 5MS
        10MS 20MS 50MS
        100MS 200MS 500MS
        1S 2S 5S
        10S 20S 50S
        100S

<a id="timebase.timebase.SiglentTimebase.GetTriggerOffset"></a>

#### GetTriggerOffset

```python
def GetTriggerOffset()
```

pySDS [TimeBase][GetTriggerOffset] : Return the delay between trigger and center point

- Pre-trigger acquisition — Data acquired before the trigger occurs. Negative trigger delays must be given in seconds.
- Post-trigger acquisition — Data acquired after the trigger has occurred

    Arguments :
        None

    Returns :
        Time in seconds

<a id="timebase.timebase.SiglentTimebase.SetTriggerOffset"></a>

#### SetTriggerOffset

```python
def SetTriggerOffset(Offset)
```

pySDS [TimeBase][SetTriggerOffset] : Offset the delay between trigger and center point.

- Pre-trigger acquisition — Data acquired before the trigger occurs. Negative trigger delays must be given in seconds.
- Post-trigger acquisition — Data acquired after the trigger has occurred

    Arguments :
        Offset : Delay in seconds to offset

    Returns :
        self.GetAllErrors()

<a id="timebase.timebase.SiglentTimebase.SetMagnifierZoom"></a>

#### SetMagnifierZoom

```python
def SetMagnifierZoom(Zoom)
```

pySDS [TimeBase][SetMagnifierZoom] : Configure the zoom on the screen.

    Arguments :
        Zoom : Two options (depending on the device !) :
            - Time with units, from 1NS to current timebase (only checked globally, not for actual settings) ==> Pass an str type
            - Factor, from 1 to 2 000 000 (Older !) ==> Pass a non str type

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid zoom

    Possibles timebases :
        1NS 2NS 5NS
        10NS 20NS 50NS
        100NS 200NS 500NS
        1US 2US 5US
        10US 20US 50US
        100US 200US 500US
        1MS 2MS 5MS
        10MS 20MS 50MS
        100MS 200MS 500MS
        1S 2S 5S
        10S 20S 50S
        100S

<a id="timebase.timebase.SiglentTimebase.SetMagnifierPosition"></a>

#### SetMagnifierPosition

```python
def SetMagnifierPosition(Position)
```

pySDS [TimeBase][SetMagnifierPosition] : Place the zoom position

    Arguments :
        Two options (depending on the device) :
            - Time position, with units. ==> Pass an str type
            - Div factor (older !) ==> Pass an non str type

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid Position

