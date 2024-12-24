ref = input("Name of the scope without SDS ?     ")
channel_nb = int(input("Number of channels      "))

with open(ref + ".toml", "w+") as f:
    f.write("[Infos]\n")
    f.write('Brand = "Siglent"\n')
    f.write(f'Device = "SDS{ref}"\n')
    f.write("\n")
    f.write("[Specs]\n")
    f.write(f"Channels = {channel_nb}\n")

    if channel_nb == 2:
        f.write('ChannelColor = ["Red", "Yellow"]\n')
    elif channel_nb == 4:
        f.write('ChannelColor = ["Red", "Yellow", "Blue", "Green"]\n')
    elif channel_nb == 8:
        f.write(
            'ChannelColor = ["Yellow", "Pink", "Light Blue", "Green", "Violet", "Blue", "Red", "Orange"]\n'
        )

    f.write("LegacyFunctions = []\n")
    f.write("BlacklistedFUnctions = []\n")
    f.write("impedance = [1000000]")
    f.write("\n")

    f.write("[Generator]\n")
    f.write("Enabled = false\n")
    f.write("\n")

    f.write("[MixedSignal]\n")
    f.write("Enabled = false\n")
    f.write("\n")

    f.write("[PowerAnalyser]\n")
    f.write("Enabled = false\n")
    f.write("\n")

print("Done !")
