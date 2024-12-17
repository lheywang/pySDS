import pyvisa
print("Hello World !")

rm = pyvisa.ResourceManager()
rm.list_resources()

# To be changed for something configurable !
instr = rm.open_resource("TCPIP0::192.168.1.5::inst0::INSTR")
print(instr)
print(instr.query('*IDN?'))