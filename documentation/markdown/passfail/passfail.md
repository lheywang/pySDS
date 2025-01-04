<a id="passfail"></a>

# passfail

<a id="passfail.passfail"></a>

# passfail.passfail

<a id="passfail.passfail.SiglentPassFail"></a>

## SiglentPassFail Objects

```python
class SiglentPassFail(SiglentBase)
```

pySDS [Files][SiglentPassFail] :    Class herited from SiglentBase.
                                    Store all command related the control of automated tests

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (14):
            ClearTests :                    Clear tests results
            EnableBuzzerOnFail :            Enable buzzer
            DisableBuzzerOnFail :           Disable buzzer
            CreateRule :                    Create new rule
            GetFramesResults :              Get results
            EnableInformationDisplay :      Show infos on screen
            DisableInformationDisplay :     Hide infos on screen
            EnablePassFailMode :            Enable mode
            DisablePassFailMode :           Disable mode
            EnableStopOnFail :              Enable stop on fail
            DisableStopOnFail :             Disable stop on fail
            Runtest :                       Run the test
            Stoptest :                      Stop the test
            SetSource :                     Set source
            SetTolerances :                 Configure tolerances

<a id="passfail.passfail.SiglentPassFail.ClearTests"></a>

#### ClearTests

```python
def ClearTests()
```

pySDS [PassFail][ClearTests] : Clear the results of the test

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.EnableBuzzerOnFail"></a>

#### EnableBuzzerOnFail

```python
def EnableBuzzerOnFail()
```

pySDS [PassFail][EnableBuzzerOnFail] : Enable the buzzer when a fail is detected

WARNING : The documentation is not clear about the real usage of this function. Use at your own risks !

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.DisableBuzzerOnFail"></a>

#### DisableBuzzerOnFail

```python
def DisableBuzzerOnFail()
```

pySDS [PassFail][DisableBuzzerOnFail] : Disable the buzzer when a fail is detected

WARNING : The documentation is not clear about the real usage of this function. Use at your own risks !

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.CreateRule"></a>

#### CreateRule

```python
def CreateRule()
```

pySDS [PassFail][CreateRule] : Create a pass fail test around the selected channel.

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.GetFramesResults"></a>

#### GetFramesResults

```python
def GetFramesResults()
```

pySDS [PassFail][GetFramesResults] : Return the number of frames that passed the test, failed and total

    Arguments :
        None

    Returns :
        List of values : Failed, Passed, Total

<a id="passfail.passfail.SiglentPassFail.EnableInformationDisplay"></a>

#### EnableInformationDisplay

```python
def EnableInformationDisplay()
```

pySDS [PassFail][EnableInformationDisplay] : Enable on the screen the information panel

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.DisableInformationDisplay"></a>

#### DisableInformationDisplay

```python
def DisableInformationDisplay()
```

pySDS [PassFail][DisableInformationDisplay] : Disable on the screen the information panel

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.EnablePassFailMode"></a>

#### EnablePassFailMode

```python
def EnablePassFailMode()
```

pySDS [PassFail][EnablePassFailMode] : Enable the pass/fail mode on the scope

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.DisablePassFailMode"></a>

#### DisablePassFailMode

```python
def DisablePassFailMode()
```

pySDS [PassFail][DisablePassFailMode] : Disable the pass/fail mode on the scope

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.EnableStopOnFail"></a>

#### EnableStopOnFail

```python
def EnableStopOnFail()
```

pySDS [PassFail][EnableStopOnFail] : Stop the scope once the first fail has been detected

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.DisableStopOnFail"></a>

#### DisableStopOnFail

```python
def DisableStopOnFail()
```

pySDS [PassFail][DisableStopOnFail] : Do not stop the scope once the first fail has been detected

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.Runtest"></a>

#### Runtest

```python
def Runtest()
```

pySDS [PassFail][RunTest] : Launch the test execution

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.Stoptest"></a>

#### Stoptest

```python
def Stoptest()
```

pySDS [PassFail][Stoptest] : Stop the test execution

    Arguments :
        None

    Returns :
        self.GetAllErrors()

<a id="passfail.passfail.SiglentPassFail.SetSource"></a>

#### SetSource

```python
def SetSource(Channel: SiglentChannel)
```

pySDS [PassFail][SetSource] : Set the source for the selftest

    Arguments :
        Channel : SiglentChannel class to be used

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid channel descriptor

<a id="passfail.passfail.SiglentPassFail.SetTolerances"></a>

#### SetTolerances

```python
def SetTolerances(X, Y)
```

pySDS [PassFail][SetTolerances] : Set the X and Y tolerances for this source (Tolerances are expressed as on screen DIV)

    Arguments :
        X : X tolerance (between 0.04 and 4)
        Y : Y tolerance (between 0.04 and 4)

    Returns :
        self.GetAllErrors()
        or
        -1 : Invalid X tolerance
        -2 : Invalid Y tolerance

