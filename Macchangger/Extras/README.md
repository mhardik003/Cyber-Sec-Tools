### To get more info : https://mhardik003.notion.site/Cyber-Sec-Tools-in-Python-c89d416c8a4b41cbabed799db2639c01
 
---

## Usage

# AUTOMATICALLY CHANGING THE MAC ADDRESS
```
ifconfig wlan0 down     # or eth0 instead of wlan0
ifconfig wlan0 hw ether <new MAC address> #make sure the address is of 12 characters
ifconfig wlan0 up       # or eth0 instead of wlan0
```
 
