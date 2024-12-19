def main():
    print("Hello World !")

    from pySDS import PySDS
    from datetime import datetime
    Dev = PySDS("192.168.1.5")

    # print(Dev.SetDate(datetime.now()))
    print(Dev.LockDevicePanel())
    print(Dev.GetDevicePanelLockState())

if __name__ == '__main__':
    main()

# Siglent Technologies,SDS824X HD,SDS08A0C802019,3.8.12.1.1.3.8
