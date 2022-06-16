import socket
import ipaddress   
import re
import requests
print("Industry Problem 1 : Computer Networks Assignment")

port_min = 0
port_max = 65535
open_ports = []

while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("VALID IP ADDRESS.")
        break
    except:
        print("INVALID IP ADDRESS!")

print("\n")

print("Location details of the entered ip address are : \n")
response = requests.post("http://ip-api.com/batch", json=[
  {"query": ip_add_entered}
]).json()
for ip_info in response:
    for k,v in ip_info.items():
        print(f"{k} : {v}")
    print("\n")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int>")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    print(port_range_valid,port_range_valid.group(1),port_range_valid.group(2))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break
    
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip_add_entered, port))
            open_ports.append(port)
    except :
        # pass
        print(f"Port {port} not open on {ip_add_entered}\t Open Ports : {open_ports}")
if len(open_ports)!=0:
    for port in open_ports:
        print(f"Port {port} is open on {ip_add_entered}.") 
else:
    print(f"No open ports from {port_min}-{port_max}")