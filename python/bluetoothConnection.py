# simple inquiry example
import bluetooth
import sys, string, os, subprocess
from client import Client

class BluetoothConnection:
    def __init__(self):
        self.found_devices = []
        self.reg_devices = []
        self.lines = []

    def get_devices(self):
        with open('devices.txt') as f:
            self.lines = f.readlines()
        for line in self.lines:
            self.reg_devices.append(line.split(','))

    def find_devices(self):
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("found %d devices" % len(nearby_devices))

        for addr, name in nearby_devices:
            self.found_devices.append((addr, name))
            print(" %s - %s" % (addr, name))
            # print(" found %s devices %s" % (found_devices, found_devices))

        # print (found_devices)
    
    def compare_devices(self):
        for device in self.found_devices:
            for d in self.reg_devices:
                print(d)
                if device[0] == d[0][0]:
                    print("Welcome %s", d[0][1])

def main():
    bConn = BluetoothConnection()
    bConn.get_devices()
    bConn.find_devices()
    # print(bConn.found_devices[0][0])
    mClient = Client(5000)
    # os.chdir("C:\\Users\\fiedramo\\source\\repos\\socketApp\\socketApp\\bin\\Debug\\net6.0-windows\\")
    # os.system(r"C:\Users\fiedramo\source\repos\socketApp\socketApp\bin\Debug\net6.0-windows\socketApp.exe")
    mClient.wait4msg()
    # os.startfile("C:\\Users\\fiedramo\\source\\repos\\socketApp\\socketApp\\bin\\Debug\\net6.0-windows\\socketApp.exe")
    
    mClient.sendmsg(bConn.found_devices[0][0])

main()