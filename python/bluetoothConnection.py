# simple inquiry example
import bluetooth
import sys, string, os, subprocess
from client import Client

class BluetoothConnection:
    def __init__(self):
        self.found_devices = []
        self.reg_devices = []
        self.reg_names = []
        self.reg_levels = []
        self.lines = []
        self.msg2send = ""

    def get_devices(self):
        with open('devices.txt') as f:
            self.lines = f.readlines()
        for line in self.lines:
            addr, name, level = line.split(',')
            self.reg_devices.append(addr)
            self.reg_names.append(name)
            self.reg_levels.append(level)

    def find_devices(self):
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        # print("found %d devices" % len(nearby_devices))

        for addr, name in nearby_devices:
            self.found_devices.append((addr, name))
            # print(" %s - %s" % (addr, name))
            # print(" found %s devices %s" % (found_devices, found_devices))

        # print (found_devices)
    
    def compare_devices(self):
        for device in self.found_devices:
            ct = 0
            if device[0] in self.reg_devices:
                while ct < len(self.reg_devices):
                    if device[0] == self.reg_devices[ct]:
                        self.msg2send = self.reg_names[ct] + ","+ self.reg_levels[ct]
                    ct += 1


def main():
    bConn = BluetoothConnection()
    bConn.get_devices()
    bConn.find_devices()
    bConn.compare_devices()
    # print(bConn.found_devices[0][0])
    mClient = Client(5000)
    os.chdir("C:\\Users\\fiedramo\\Desktop\\Spring_2023\\Uni\\CS484-HCI\\Proj-21-3\\DeafSignAR\\socketApp\\socketApp\\bin\\Debug\\net6.0-windows")
    os.system("C:\\Users\\fiedramo\\Desktop\\Spring_2023\\Uni\\CS484-HCI\\Proj-21-3\\DeafSignAR\\socketApp\\socketApp\\bin\\Debug\\net6.0-windows\\socketApp.exe")
    mClient.wait4msg()
    # os.startfile("C:\\Users\\fiedramo\\source\\repos\\socketApp\\socketApp\\bin\\Debug\\net6.0-windows\\socketApp.exe")
    mClient.sendmsg(bConn.msg2send)

main()