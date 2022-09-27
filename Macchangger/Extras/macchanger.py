'''
-------------------------------------------------------------------------
PROGRAM TO CHANGE THE MAC ADDRESS OF AN INTERFACE USING TERMINAL COMMANDS
-------------------------------------------------------------------------
'''


#!/usr/bin/env python3

import subprocess # using the subprocess module (to execute the system commands)

''' 
using function 'call' : runs the commands in foreground and thus waits
for the command to  finish before moving to the next line and this is 
very necessary for this exercise becasue thats what we want in this program
'''

#subprocess.call("ifconfig", shell=True)  
subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell=True) #chasnge the mac address as per your need
subprocess.call("ifconfig wlan0 up", shell=True)
#subprocess.call("ifconfig",shell=True)


