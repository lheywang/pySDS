# ============================================================================================================
# 3. Trigger.py
# lheywang on 04/01/2025
#
# Show how to use the package to open an instance and how to configure some triggering options.
#
# ============================================================================================================

import SDSPy


def main():
    Dev = SDSPy.PySDS("192.168.1.5")  # Define your instrument IP here
    # Check return value AND / OR console messages for errors

    if Dev.DeviceOpenned != 1:
        print("Failed to open the device")  # Handle your errors here
        return -1

    Dev.Channel[0].DisableTrace()           # Enable drawing of the trace
    Dev.Channel[0].SetCoupling("D")         # Configure the channel to DC
    # Here we don't care about display config since the trace is hidden

    Dev.Trigger.SetLevel1(Dev.Channel[0], 0.5) # Here we configure the trigger on Channel0 at 500mV
    Dev.Trigger.SetSlope("POS")             # Setting rising edges

    return  # Once done, only exit the function.
    # All of the nasty stuff is automatically handled by PyVISA, the package used to communicate with the device.


if __name__ == "__main__":
    main()