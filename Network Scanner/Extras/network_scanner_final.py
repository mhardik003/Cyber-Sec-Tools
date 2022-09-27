#!/bin/usr/env python3
from requests import get
import scapy.all as scapy
import subprocess


def scan_IPs(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list=[]
    for element in answered_list:
        client_dict={"IP":element[1].psrc,"MAC":element[1].hwsrc}
        clients_list.append(client_dict)
    
    
    return clients_list

def print_MAC(clients_list):
    print("Number of clients found : ",len(clients_list))
    print("IP\t\t\tMAC\n-----------------------------")
    for client in client_lists:
        print (client["IP"],"\t\t",client["MAC"])

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
client_lists = scan_IPs(curr_IP+"1/24")
print_MAC(client_lists)
