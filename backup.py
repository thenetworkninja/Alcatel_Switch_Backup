#!/usr/bin/env python3

from netmiko import ConnectHandler
import time

# getting system date
day = time.strftime('%d')
month = time.strftime('%m')
year = time.strftime('%Y')
today = month + "_" + day + "_" + year
# initializing device
device = {
    'device_type': 'alcatel_sros',
    'ip': '192.168.100.254',
    'username': 'admin',
    'password': 'switch',
}
# opening IPlist.txt file
ipfile = open("iplist.txt")
print("Script to take backup of devices in IPlist.txt file")

# Taking Backup
for line in ipfile:
    try:
        device['ip'] = line.strip("\n")
        print("\nConnecting Device ", line)
        connect = ConnectHandler(**device)
        print("Reading the running config ")
        output = connect.send_command_timing('write terminal', 2)

        filename = device['ip'] + '_' + today + ".txt"
        saveConfig = open(filename, 'w+')

        print("Writing Configuration to file")
        saveConfig.write(output)

        saveConfig.close()

        connect.disconnect()

        print("Configuration saved to file", filename)

    except:

        print("\nAccess to " + device['ip'] + " failed, unable to take backup of " + device['ip'])

        ipfile.close()
        break


print("\nAll devices are backup successfully")