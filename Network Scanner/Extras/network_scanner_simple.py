#!/bin/usr/env python3

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("192.168.1.1/24") # 10.2.128.1 is the router of the network