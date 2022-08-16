#!/usr/bin/env python

from tabnanny import verbose
import scapy.all as scapy

import socket


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list, unanswered_list = scapy.srp(
        arp_request_broadcast, timeout=1, verbose=False)
    clients_list = []

    for answer in answered_list:
        client_dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list


def print_clients_list(clients_list):
    print("IP\t\t\tMAC Address\n------------------------------------")
    for client in clients_list:
        print(client["ip"], "\t\t", client["mac"])


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IPAddr = s.getsockname()[0]
last_dot = IPAddr.rfind(".")
mod_IP = IPAddr[0:last_dot+1]+"1/24"
clients_list = scan(mod_IP)
print_clients_list(clients_list)
