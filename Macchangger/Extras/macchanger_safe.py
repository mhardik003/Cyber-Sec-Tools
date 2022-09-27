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


'''
TO MAKE THE PROGRAM MORE SECURE
i.e. such that user doesnt put any other commands instead of the expected interfac
Exmaple : "wlan0;ls;"
'''

print("\n[+] Changing MAC address for " + interface + " to " + newmac)

#subprocess.call(["ifconfig"])
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",newmac])
subprocess.call(["ifconfig",interface,"up"])
#subprocess.call(["ifconfig"])


print("[+] Done!")
