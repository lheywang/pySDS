# PySDS
PySDS is a Python package to exploit functionnalities of the Siglent SDS Oscilloscopes.

## Installation :
You can simply do :
> pip install SDSpy

Or, you can download the .whl package and install it by hand 
> pip install SDSpy[. . .].whl

## Basic usage :
Here an extract of the example 1. Openning, how to use the lib 

> import SDSPy
> 
> Dev = SDSPy.PySDS("192.168.1.5")  
> 
> if Dev.DeviceOpenned != 1:
>     print("Failed to open the device") 
>     return -1
> 
> Dev.Channel[0].EnableTrace()            
> Dev.Channel[0].SetCoupling("D")    

More advanced documentation is available on : 

## More advanced usages
All of the documentation is available on GitHub, at this link : [Documentation.md](https://github.com/lheywang/SDSpy/blob/Main/documentation/Documentation.md)

I'll describe everything you need to know !
