# OVERVIEW - MAC : (Media Access Control)

Permanent, Phusical and Unique
Assigned by manufacture and thus specific to each device module and therefore is used to identify computers 

IP : used in internet to indetify and comunicate between devices on the internet

MAC address : used within the network to identiy devices and transfer data between hthe devices
Contains a source AMC and destination MAC

## WHY CHANGE THE MAC ADDRES?
* To make yourself anonymuos on the network
* Impersonate other devices( thereby gaining permission assigned to them)
* Bypassing filters

lo : virtual interface created by linux
etho0 :ethernet
wlan0 : wifi

in ifconfig
INET : gives the IP
netmask : netmask
broadcast : broadcast
ETHER :  Mac address



# AUTOMATICALLY CHANGING THE MAC ADDRESS
```
ifconfig wlan0 down     # or eth0 instead of wlan0
ifconfig wlan0 hw ether <new MAC address> #make sure the address is of 12 characters
ifconfig wlan0 up       # or eth0 instead of wlan0
```
 