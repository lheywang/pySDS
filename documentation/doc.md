# PySDS
PySDS is a Python package to exploit functionnalities of the Siglent SDS Oscilloscopes.

As the official Siglent document, some devices are available : 
- Digital Oscilloscopes Series
- SDS1000CML/CML+
- SDS1000DL/DL+
- SDS1000CNL/CNL+
- SDS1000/1000X/1000X-S/1000X+/1000X-E
- SDS2000/SDS2000X

And some SPO series : 
- SDS1000X/1000X+/SDS1000X-E
- SDS2000/2000X
- SDS800X

Due to financial cost of theses devices, I can only test it with my own device, an Siglent SDS824X-HD. 
Thus, this package can only be certified for THIS device, and ONLY THIS one. Others seems to respond to their standard command set, and thus shall be working flawlessly, but I can't test it.

## How is the command set organized ?
The official Siglent command set is a bit complex, since some functions are applied on the overall device, where other are per trace (= channel).
That's why this package include in fact multiple subclass, one per object, which are then linked into a big class.
