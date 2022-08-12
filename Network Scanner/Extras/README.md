# NETWORK SCANNER
## Will scan IP addresses and MAC addresses(similar to netdiscover)

Need to gather info about devices

What Network Scanner does is:
* Discover all devices on the network
* Display their IP Address
* Display their MAC address


<br>
-----------------------------------------------
## SOME USEFUL LINUX COMMANDS
```
route -n
ifconfig
netdiscover
nmap
```

<br>

-------------------------------------------------

## COMMAND TO USE NETDISCOVER IN TERMINAL
```
netdiscover -r 10.2.131.0/24 #whatever ip you have
```
Note : This will scan all IPs from 10.2.131.0 to 10.2.131.254


<br>

-----------------------------------------------------
## ARP (Address Resolution Protocol)
Allows to link IP addresses with MAC addresses 

* by sending a broadcast message [called ARP request] (broadcast MAC address)
* the device with the matching IP will respond to the request by giving it its MAC address

Therefore will manually making the network scanner we will send an ARP request to all the IP addresses on the connceted network. So everytime we send the broadcast if some device is connected to that IP address it will respond to the ARP request, saying i have this IP address and my MAC address is this, if not then nothing happens and we will move on to the next IP

--------------------------------------------------
## SOME EXPLANATION FOR network_scanner_moderate.py
STEPS going to be used
* Create ARP request to broadcast MAC asking for IP
* Send packet and receive response
* Parse the response
* Print result

### Using Scapy to create a packet
The packet broadly does two tasks
* Use ARP to ask who has a specific IP
* Set destinationo MAC to broadcast MAC