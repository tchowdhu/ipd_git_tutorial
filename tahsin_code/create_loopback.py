#! /usr/bin/env python

#import library
from getpass import getpass
from netmiko import ConnectHandler

#Device login info 
CISCO_CSR_XE_HOST = 'sandbox-iosxe-latest-1.cisco.com'
USERNAME='developer'
PASSWORD=getpass('\nEnder password for {}@{}: '.format(USERNAME, 
CISCO_CSR_XE_HOST))

device = {
    'device_type' : 'cisco_ios',
    'ip' : CISCO_CSR_XE_HOST,
    'username' : USERNAME,
    'password' : PASSWORD
}

# Connect device and run command 
device = ConnectHandler(**device)

commands = ['interface loopback40',
            'ip address 40.40.40.40 255.255.255.255']

output = device.send_config_set(commands) 
print()
print(output)
output = device.send_command("show ip interface brief\n")
print()
print (output)
print()
device.disconnect()
