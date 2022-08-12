#!/bin/usr/env python3
import scapy.all as scapy
import subprocess

def scan_IPs(ip):
    arp_request = scapy.ARP(pdst=ip)  # OR arp_request.pdst=ip
    # arp_request.show()
    # print(arp_request.summary()) # OUTPUT : ARP who has <ip> says <your ip>

    # scapy.ls(scapy.ARP) #list all all functions in scapy.ARP
    '''
    hwtype     : XShortField                         = (1)
    ptype      : XShortEnumField                     = (2048)
    hwlen      : FieldLenField                       = (None)
    plen       : FieldLenField                       = (None)
    op         : ShortEnumField                      = (1)
    hwsrc      : MultipleTypeField                   = (None)
    psrc       : MultipleTypeField                   = (None)
    hwdst      : MultipleTypeField                   = (None)
    pdst       : MultipleTypeField                   = (None)
    '''

    # creates an ethernet object
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    # OR broadcast.dst="ff:ff:ff:ff:ff:ff"
    # print(broadcast.summary()) #f8:89:d2:7c:09:99 > ff:ff:ff:ff:ff:ff (0x9000)
    # to make sure the packet we are sending is being sent to the broadcast MAC address and not to only device
    # scapy.ls(scapy.Ether())
    '''
    dst        : DestMACField                        = 'ff:ff:ff:ff:ff:ff' (None)
    src        : SourceMACField                      = 'f8:89:d2:7c:09:99' (None)
    type       : XShortEnumField                     = 36864           (36864)
    '''
    # now we want to set the destination MAc to the mac address of the broadcast

    # / combination of both the functions
    arp_request_broadcast = broadcast/arp_request
    # Ether / ARP who has Net('10.2.128.1/24') says 10.2.131.78
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()

    # SRP : send and receive packets with a custom ether part unlike sr
    # here verbose = False just cleans the output (removes some info thatsrp prints like number of packets recived etc.)
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    # since srp returns a tuple of two lists containing the answered packets and the unanswered packets
    # timeout = 1 makes the function wait for 1 second for the request, if it doesnt get any recieve any response, it moves on to the next ip
    # print(answered_list.summary())
    # print(unanswered_list.summary())
    # here again answered list has a tuple of two elements : first element is the ARP req sent by us and second is the reponse by the other computer
    # therefore we are only intrested in the second element of the tuple

    print("IP\t\t\tMAC Addres")
    print("----------------------------------")
    for element in answered_list:
        print(element[1].psrc,"\t\t",element[1].hwsrc)
        # print(element[0].show())
        # print(element[1].show())
        # print("IP of target : " , element[1].psrc) #ip of src of the response
        # print("MAC of the target : " , element[1].hwsrc) #hardware(MAC) of source of the response
        # print("====================================")

def get_curr_IP():    
    curr_IP= str(subprocess.check_output("hostname -I | awk '{print $1}'",shell=True))
    curr_IP=curr_IP[2:]
    curr_IP=curr_IP[:-3]
    print("Your current IP is ",curr_IP)
    while(curr_IP[-1]!="."):
        curr_IP=curr_IP[:-1]
    
    return curr_IP

curr_IP=get_curr_IP()
print("Scanning the IPs ",curr_IP+"1/24")
scan_IPs(curr_IP+"1/24")
