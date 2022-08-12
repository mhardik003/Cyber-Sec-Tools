'''
-------------------------------------------------------------------------
PROGRAM TO CHANGE THE MAC ADDRESS OF ANY INTERFACE USING ARGUMENTS
-------------------------------------------------------------------------
'''

'''
SAMPLE LINE TO EXECUTE THE FILE : sudo python3 maccchanger_args_functions.py -i wlp4s0 -m 00:11:22:33:44:55
'''


#!/usr/bin/env python3

# using the subprocess module (to execute the system commands)

# module that will  allow to get arguements from the user and parse them and use them in the code




import subprocess
import optparse
def get_arguements():
    # OptionParse is a class so parser is a object of that class
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="newmac",
                      help="New MAC address")

    # will return two sets of info options and args
    (options, arguements) = parser.parse_args()
    if not options.interface:  # if -i not given
        parser.error(
            "[-] Please specify an interface, use --help for more info")
    elif not options.newmac:  # if -m not given
        parser.error("[-] Please specify a new mac, use --help for more info")

    return options


def change_mac(interface, new_mac):
    print("\n[+] Changing MAC address for " + interface + " to " + new_mac)

    # subprocess.call(["ifconfig"])
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    # subprocess.call(["ifconfig"])

    print("[+] Done!")


options = get_arguements()

change_mac(options.interface, options.newmac)
