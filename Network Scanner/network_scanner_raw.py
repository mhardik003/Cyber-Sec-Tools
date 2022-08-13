#!/usr/bin/env python

from tabnanny import verbose
import scapy.all as scapy
import pprint
import socket   
# --------- CAN BE DONE BY JUST USING THIS CODE-------------
"""
def scan(ip):
    scapy.arping(ip)
    

scan("10.2.129.1/24")
"""


def scan(ip):
    # CREATING THE ARP REQUEST
    # pdst is the IPField (p-dest) whose original value is 0.0.0.0 so we have to set it to "ip"
    arp_request = scapy.ARP(pdst=ip)
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP()) # will give a list of all the fields that can be set along with the description and their default values

    # CREATING AN ETHERNET FRAME THAT WILL BE SENT TO THE BROADCAST MAC ADDRESS
    # creates an ethernet object from scapy and stores it in broadcast
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())

    # COMBINING THE TWO PACKETS
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()

    # SENDING THE ARP BROADCAST REQUEST
    # srp : send and request with a custom ether part
    # returns a couple of two lists - answered packets and unanswered packets
    # timeout = 1 is that it will for 1 second before moving on to the next IP in case it doesn't get a response
    answered_list, unanswered_list = scapy.srp(
        arp_request_broadcast, timeout=1, verbose=False)
    # answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    # print(answered_list.summary())

    # PARSING THE RESPONSE (answered_list variable)

    clients_list = []
    # print("IP\t\t\tMAC Address\n------------------------------------")
    for answer in answered_list:
        # print(answer,"\n----------------------------------") # it is a couple of (packet sent, answer)
        """ (<Ether  dst=ff:ff:ff:ff:ff:ff type=ARP |<ARP  pdst=10.2.129.40 |>>, <Ether  dst=00:32:11:00:23:d7 src=00:2a:10:09:d9:d0 type=ARP |<ARP  hwtype=0x1 ptype=IPv4 hwlen=6 plen=4 op=is-at hwsrc=ea:83:ba:ac:33:2e psrc=10.2.129.40 hwdst=00:32:11:00:23:d7 pdst=10.2.129.242 |>>)"""
        # print(answer[1].show())  # will just print the answer
        """
        ###[ Ethernet ]### 
            dst       = 00:32:11:00:23:de
            src       = d0:37:45:b4:ab:00
            type      = ARP
        ###[ ARP ]### 
            hwtype    = 0x1
            ptype     = IPv4
            hwlen     = 6
            plen      = 4
            op        = is-at
            hwsrc     = d0:37:45:b4:ab:0b
            psrc      = 10.2.129.32
            hwdst     = 00:32:11:00:23:d7
            pdst      = 10.2.129.242
            ###[ Padding ]### 
            load      = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        None
        """
        client_dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        clients_list.append(client_dict)
        # print(answer[1].hwsrc,"\n",answer[1].psrc,"\n==============") # hardware of source of repone and ip of source of response
        # print(answer[1].psrc+"\t\tx`"+answer[1].hwsrc)

    # pprint.pprint(clients_list)
    return clients_list

def print_clients_list(clients_list):
    print("IP\t\t\tMAC Address\n------------------------------------")    
    for client in clients_list:
        print(client["ip"],"\t\t",client["mac"])


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IPAddr = s.getsockname()[0]
last_dot = IPAddr.rfind(".")
mod_IP=IPAddr[0:last_dot+1]+"1/24"
clients_list=scan(mod_IP)
print_clients_list(clients_list)