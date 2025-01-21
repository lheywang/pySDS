# ============================================================================================================
# 3. Trigger.py
# lheywang on 04/01/2025
#
# Show how to use the package to open an instance and how to configure some triggering options.
#
# ============================================================================================================

import SDSPy
import time


def main():
    Dev = SDSPy.PySDS("172.16.1.2")  # Define your instrument IP here
    # Check return value AND / OR console messages for errors

    if Dev.DeviceOpenned != 1:
        print("Failed to open the device")  # Handle your errors here
        return -1

    Dev.Channel[0].EnableTrace()  # Enable drawing of the trace
    Dev.Channel[0].SetCoupling("D")  # Configure the channel to DC

    Dev.Channel[1].EnableTrace()  # Enable drawing of the trace
    Dev.Channel[1].SetCoupling("D")  # Configure the channel to DC

    Dev.Measure.SetMeasure("MEAN", Dev.Channel[0]) # Configure a measure
    Dev.Measure.SetMeasure("PKPK", Dev.Channel[0]) # Configure another measure
    Dev.Measure.SetDelayMeasure("PHA", Dev.Channel[0], Dev.Channel[1]) # Configure a measure from the time domain

    print(Dev.Measure.GetMeasure("MEAN", Dev.Channel[0])) # Read one measure

    # Dev.Measure.EnableMeasureStatistics() # Set statistics
    # 
    # time.sleep(1)
    # print(Dev.Measure.GetStatsMeasure(1)) # Get stats for the first installed measure, here "PKPK" --> The order is different than the one configured !

    return  # Once done, only exit the function.
    # All of the nasty stuff is automatically handled by PyVISA, the package used to communicate with the device.


if __name__ == "__main__":
    main()
