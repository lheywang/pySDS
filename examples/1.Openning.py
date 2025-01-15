# ============================================================================================================
# 1.Openning.py
# lheywang on 21/12/2024
#
# Show how to use the package to open an instance and use it
#
# ============================================================================================================

import SDSPy


def main():
    Dev = SDSPy.PySDS("192.168.1.5")  # Define your instrument IP here
    # Check return value AND / OR console messages for errors

    if Dev.DeviceOpenned != 1:
        print("Failed to open the device")  # Handle your errors here
        return -1

    # ...
    # ...

    return  # Once done, only exit the function.
    # All of the nasty stuff is automatically handled by PyVISA, the package used to communicate with the device.


if __name__ == "__main__":
    main()
