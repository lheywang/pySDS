<a id="display"></a>

# display

<a id="display.display"></a>

# display.display

<a id="display.display.SiglentScreen"></a>

## SiglentScreen Objects

```python
class SiglentScreen(SiglentBase)
```

pySDS [Display][SiglentScreen] :    Class herited from SiglentBase.
                                    Store all command related the control of display.

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (7):
            EnableScreenInterpolation :         Enable continuous display of the tracks
            DisableScreenInterpolation :        Enable the display of only points
            SelectGrid :                        Select the grid type
            SetIntensity :                      Select the trace and grid intensity
            ShowMenu :                          Show menu
            HideMenu :                          Hide menu
            ConfigurePersistence :              Configure trace persistence

<a id="display.display.SiglentScreen.EnableScreenInterpolation"></a>

#### EnableScreenInterpolation

```python
def EnableScreenInterpolation()
```

pySDS [Screen][EnableScreenInterpolation] : Enable the drawing of lines between data points

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="display.display.SiglentScreen.DisableScreenInterpolation"></a>

#### DisableScreenInterpolation

```python
def DisableScreenInterpolation()
```

pySDS [Screen][DisableScreenInterpolation] : Disable the drawing of lines between data points

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="display.display.SiglentScreen.SelectGrid"></a>

#### SelectGrid

```python
def SelectGrid(Grid)
```

pySDS [Screen][SelectGrid] : Select the grid on the display

    Arguments :
        Grid : FULL | HALF | OFF

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid grid mode

<a id="display.display.SiglentScreen.SetIntensity"></a>

#### SetIntensity

```python
def SetIntensity(Grid, Trace)
```

pySDS [Screen][Intensity] : Set intensity of the grid display

    Arguments :
        Grid : Value for the grid. 0 to 100
        Trace : Value for the trace. 0 to 100

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid grid value
        -2 : Invalid trace value

<a id="display.display.SiglentScreen.ShowMenu"></a>

#### ShowMenu

```python
def ShowMenu()
```

pySDS [Screen][ShowMenu] : Show the menu on the screen

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="display.display.SiglentScreen.HideMenu"></a>

#### HideMenu

```python
def HideMenu()
```

pySDS [Screen][HideMenu] : Hide the menu on the screen

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="display.display.SiglentScreen.ConfigurePersistence"></a>

#### ConfigurePersistence

```python
def ConfigurePersistence(Value)
```

pySDS [Screen][ConfigurePersistence] : Configure the persistence of the track on the screen

WARNING : OFF may not be available for all of the models.

    Arguments :
        Value : INFINITE | 1 | 5 | 10 | 30 | (OFF)

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid persistence value

