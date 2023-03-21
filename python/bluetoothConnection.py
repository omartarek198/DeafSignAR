# simple inquiry example
import bluetooth

found_devices = []
reg_devices = []
lines = []

with open('devices.txt') as f:
    lines = f.readlines()

for line in lines:
    reg_devices.append(line.split(','))


def find_nearby():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        found_devices.append((addr, name))
        print(" %s - %s" % (addr, name))
        # print(" found %s devices %s" % (found_devices, found_devices))
    
    print (found_devices)
    
find_nearby()

def compare_devices():
    for device in found_devices:
        for d in reg_devices:
            print(d)
            if device[0] == d[0][0]:
                print("Welcome %s", d[0][1])

compare_devices()