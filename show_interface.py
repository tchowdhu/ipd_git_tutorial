#! /usr/bin/env python

#import library
from getpass import getpass
from netmiko import ConnectHandler

#Device login info 
CISCO_CSR_XE_HOST = 'sandbox-iosxe-latest-1.cisco.com'
USERNAME='developer'
PASSWORD=getpass('\nEnder password for {}@{}: '.format(USERNAME, CISCO_CSR_XE_HOST))

device = {
    'device_type' : 'cisco_ios',
    'ip' : CISCO_CSR_XE_HOST,
    'username' : USERNAME,
    'password' : PASSWORD
}

# Connect device and run command to show all the ip interfaces
device = ConnectHandler(**device)
output = device.send_command("show ip interface brief")
print()
print (output)
print()
device.disconnect()
