#!/usr/bin/env python

import socket
import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)
    
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IPAddr = s.getsockname()[0]
last_dot = IPAddr.rfind(".")
mod_IP = IPAddr[0:last_dot+1]+"1/24"
scan(mod_IP)
