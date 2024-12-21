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

## How is the command set organized ?
Their official programming guide which may be found linked into the source folder of the documentation explain all of this.
They splitted the functions per category, so, I just did the same.

There is one main class, and then composition with subclass. Each subclass is a category on the document, and is focused on ONE functionnality. Each function correspond to one, and only SCPI command.

For example, to configure the trigger of the device, you'll need to :
> Device.trigger.SetThreshold(...)

And, in addition of that, I've included custom build function that group multiple functions calls.
For example, you can do : 
> Device.trigger.configure(...)
This function will do all of the required calls to configure the trigger, without needing you to call a ton of functions.

Generally, theses functions are name on the following chart :
- Read / Set : Single SCPI functions
- Configure / Get : Groupe of previous functions

## Examples
There is some examples on the source repo (linked in the .tar.gz file), if you need some more specific explanations !
Take a look at them :
- 1.Openning a device
- 2.Configuring a device
- 3.Reading from a device