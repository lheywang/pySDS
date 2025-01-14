# ============================================================================================================
# 2. SimpleConfigure.py
# lheywang on 04/01/2025
#
# Show how to use the package to open an instance and do a simple configuration it.
#
# ============================================================================================================

import SDSPy


def main():
    Dev = SDSPy.PySDS("192.168.1.5")  # Define your instrument IP here
    # Check return value AND / OR console messages for errors

    if Dev.DeviceOpenned != 1:
        print("Failed to open the device")  # Handle your errors here
        return -1

    Dev.Channel[0].EnableTrace()  # Enable drawing of the trace
    Dev.Channel[0].SetCoupling("D")  # Configure the channel to DC
    Dev.Channel[0].SetOffset(1)  # Configure offset on display
    Dev.Channel[0].SetTraceDIV(
        0.5
    )  # Configure size of drawing, here 500mV per division.

    return  # Once done, only exit the function.
    # All of the nasty stuff is automatically handled by PyVISA, the package used to communicate with the device.


if __name__ == "__main__":
    main()
