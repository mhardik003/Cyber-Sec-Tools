'''
USAGE : sudo macchanger.py -i <interface name> -m <new MAC address>
'''


# Refer to : https://mhardik003.notion.site/Cyber-Sec-Tools-in-Python-c89d416c8a4b41cbabed799db2639c01

# Refer to the subprocess documentation at : https://docs.python.org/3/library/subprocess.html


# CALL : runs the command in the foreground and waits for the command to finish before moving on to the next line
# (which is what we want)


#!/usr/bin/env python3
import subprocess
import optparse


def get_arguements():
    interface = ""
    new_mac_addr = ""

    # INPUT
    # interface = input("interface > ")
    # new_mac_addr = input("new MAC > ")

    # USING COMMAND LINE ARGUEMENTS
    parser = optparse.OptionParser()  # parser object (it will handle user input)
    # dest is the name where the value will be stored
    parser.add_option("-i", "--interface", dest="interface",
                    help="Interface whose MAC address you want to change")
    parser.add_option("-m", "--mac", dest="new_mac_addr", help="New MAC address")
    
    (options, arguements) = parser.parse_args() #options will contains the input and arguements will contains --interface and --mac
    if(not options.interface):
        # print("Error : Interface not input")
        # exit(0)
        parser.error("[-] Please specify an interface, use --help for more info")
    if(not options.new_mac_addr):
        # print("Error : MAC Address not input")
        # exit(0)
        parser.error("[-] Please specify a new MAC address, use --help for more info")

    return (options.interface, options.new_mac_addr)


def change_mac(interface, new_mac_addr):
    print("[+] Changing the MAC address for " + interface + " to " + new_mac_addr)

    # print("Previous MAC address :",)
    # subprocess.call("ifconfig "+interface +
    # " | grep -i 'ether' | awk '{print $2}'", shell=True)


    # -----------DONT DO IT LIKE THIS-------------------
    # subprocess.call("ifconfig "+interface+" down", shell=True)
    # subprocess.call("ifconfig "+interface + " hw ether "+new_mac_addr, shell=True)
    # subprocess.call("ifconfig "+interface+" up", shell=True)
    # # print("\nNew MAC address :",)
    # subprocess.call("ifconfig "+interface + " | grep -i 'ether' | awk '{print $2}'", shell=True)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw",
                    "ether", new_mac_addr])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Done!")





(interface, new_mac_addr)=get_arguements()

change_mac(interface, new_mac_addr)