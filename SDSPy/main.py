def main():
    print("Hello World !")

    import pySDS
    from datetime import datetime

    Dev = pySDS.PySDS("192.168.1.5")

    if Dev.DeviceOpenned == 0:
        print("Device not openned. Exiting...")
        exit()

    # print(Dev.SetDate(datetime.now()))
    print(Dev.Trigger.SetCoupling("C3", "AC"))
    print(Dev.Trigger.SetPattern(["C1", "C2"], ["L", "H"], "AND"))
    print(Dev.Trigger.GetPattern())


if __name__ == "__main__":
    main()

# Siglent Technologies,SDS824X HD,SDS08A0C802019,3.8.12.1.1.3.8
