# PySDS
PySDS is a Python package to exploit functionnalities of the Siglent SDS Oscilloscopes.

## Installation :
You can simply do :
> pip install SDSpy

Or, you can download the .whl package and install it by hand 
> pip install SDSpy[. . .].whl

## Compatible devices
Siglent are a bit weird on their programming guide, since they do not share a programming guide per device. They only a global file.
Thus, it's difficult to identify any issues that are related to the software.

Nonetheless, the excluded devices seems not to be available anymore, so we can just consider them as obsolete.
And, all of the compatibles devices seems to be issues from their latest range, and we can probably assume that all of the commands are the same, excepted for some parameters.

Due to financial cost of theses devices, I can only test it with my own device, an Siglent SDS824X-HD. 
Thus, this package can only be certified for THIS device, and ONLY THIS one. Others seems to respond to their standard command set, and thus shall be working flawlessly, but I can't test it.

To any user that own one of the device, I'm open for your feedback / suggestions and so to verify my work / include new functions !

To track theses changes, make a tour on : [Compatibility.md](https://github.com/lheywang/SDSpy/blob/Main/documentation/Compatibility.md)

## How is the command set organized ?
Their official programming guide which may be found linked into the source folder of the documentation explain all of this.
They splitted the functions per category, so, I just did the same.

There is one main class, and then composition with subclass. Each subclass is a category on the document, and is focused on ONE functionnality. Each function correspond to one, and only SCPI command.

To this day, there is the followings functions :
- acquisition control
- channel control
- communication settings (network configuration excluded)
- cursor placement
- serial bus decoding control
- digital channel control
- waveform export to BMP
- maths operations
- automatic measures control
- autotest with a pass-fail condition
- references control
- triggering control
- waveform export as a list of points

For example, to configure the trigger of the device, you'll need to :
> Dev.Trigger.SetLevel1(Device.Channel[0], 0.5)

Globally, this is : 
> [Device].[Function_name].[Function](Arguments)

## How is the documentation organized ?
The documentation start with this page [SDSPy.md](https://github.com/lheywang/SDSpy/blob/Main/documentation/markdown/SDSPy.md).
Then, there is folders per functionnality of the scope, for example : One folder for the trigger submenu, and one for the cursor...

Documentation was build using pydoc-markdown package, which extract doc from docstrings in the source code.

## Examples
There is some examples on the source repo (linked in the .tar.gz file), if you need some more specific explanations !
Take a look at them :
- 1.Openning a device
- 2.Configuring a device
- 3.Doing some maths on the channels
- 4.Configure Triggering behvaviors.