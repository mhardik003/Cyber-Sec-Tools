'''
-------------------------------------------------------------------------
PROGRAM TO CHANGE THE MAC ADDRESS OF ANY INTERFACE USING TERMINAL COMMANDS
-------------------------------------------------------------------------
'''

#!/usr/bin/env python3
# using the subprocess module (to execute the system commands)
import subprocess


interface = input("interface > ")
newmac = input("new MAC > ")

print("\n[+] Changing MAC address for " + interface + " to " + newmac)

#subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig "+interface+" down", shell=True)
# chasnge the mac address as per your need
subprocess.call("ifconfig "+interface+" hw ether "+newmac, shell=True)
subprocess.call("ifconfig "+interface+" up", shell=True)
# subprocess.call("ifconfig",shell=True)

print("[+] Done!")
