'''
USAGE : sudo macchanger.py -i <interface name> -m <new MAC address>
'''
# Refer to : https://mhardik003.notion.site/Cyber-Sec-Tools-in-Python-c89d416c8a4b41cbabed799db2639c01

#!/usr/bin/env python3
import subprocess
import optparse


def get_arguements():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",help="Interface whose MAC address you want to change")
    parser.add_option("-m", "--mac", dest="new_mac_addr",help="New MAC address")
    (options, arguements) = parser.parse_args()
    if (not options.interface):
        parser.error("[-] Please specify an interface, use --help for more info")
    if (not options.new_mac_addr):
        parser.error("[-] Please specify a new MAC address, use --help for more info")

    return (options.interface, options.new_mac_addr)


def change_mac(interface, new_mac_addr):
    print("[+] Changing the MAC address for " +interface + " to " + new_mac_addr)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw","ether", new_mac_addr])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Done!")


(interface, new_mac_addr) = get_arguements()
change_mac(interface, new_mac_addr)
