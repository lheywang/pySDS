<a id="Files"></a>

# Files

<a id="Files.files"></a>

# Files.files

<a id="Files.files.SiglentFiles"></a>

## SiglentFiles Objects

```python
class SiglentFiles(SiglentBase)
```

pySDS [Files][SiglentFiles] :   Class herited from SiglentBase.
                                Store all command related the control of filesystem.

    Attributes :
        Herited from SiglentBase

    Methods :
        Private (0) :
            None

        Public (7):
            CaptureBMPScreen :          Capture the screen as a BMP File

<a id="Files.files.SiglentFiles.CaptureBMPScreen"></a>

#### CaptureBMPScreen

```python
def CaptureBMPScreen(File)
```

pySDS [Files][CaptureBMPScreen] : Capture the screen and write a BMP file

    Arguments :
        File : Path to be written

    Returns :
        self.GetAllErrors()

