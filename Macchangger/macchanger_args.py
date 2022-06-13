'''
-------------------------------------------------------------------------
PROGRAM TO CHANGE THE MAC ADDRESS OF ANY INTERFACE USING ARGUMENTS
-------------------------------------------------------------------------
'''

#!/usr/bin/env python3

# using the subprocess module (to execute the system commands)
import subprocess

# module that will  allow to get arguements from the user and parse them and use them in the code
import optparse 


# OptionParse is a class so parser is a object of that class
parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface",
                  help="Interface to change its MAC address")


parser.add_option("-m", "--mac", dest="newmac",
                  help="New MAC address")


# will return two sets of info options and args
(options, arguements) = parser.parse_args()
interface = options.interface
newmac = options.newmac

print("\n[+] Changing MAC address for " + interface + " to " + newmac)

# subprocess.call(["ifconfig"])
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
subprocess.call(["ifconfig", interface, "up"])
# subprocess.call(["ifconfig"])


print("[+] Done!")
