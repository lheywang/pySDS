# ============================================================================================================
# 3. Trigger.py
# lheywang on 04/01/2025
#
# Show how to use the package to open an instance and how to configure some triggering options.
#
# ============================================================================================================

import SDSPy


def main():
    Dev = SDSPy.PySDS("172.16.1.2")  # Define your instrument IP here
    # Check return value AND / OR console messages for errors

    if Dev.DeviceOpenned != 1:
        print("Failed to open the device")  # Handle your errors here
        return -1

    Dev.Channel[0].DisableTrace()  # Enable drawing of the trace
    Dev.Channel[0].SetCoupling("D")  # Configure the channel to DC
    # Here we don't care about display config since the trace is hidden

    # This function return extremely large arrays ! 
    # I recommend to decimate them, or to treat them with specific tools (cudf, np, pandas...)
    Val, Time = Dev.Waveform.GetWaveformData(Dev.Channel[0], 2, 1, 0.01, 100000000)

    return  # Once done, only exit the function.
    # All of the nasty stuff is automatically handled by PyVISA, the package used to communicate with the device.


if __name__ == "__main__":
    main()
