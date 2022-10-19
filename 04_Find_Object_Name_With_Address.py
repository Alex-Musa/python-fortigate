from operator import truediv
from netmiko import Netmiko
import re

search = input("Enter IP to Search: ")
ip_pattern = re.compile(r"edit (.+)")


FW1 = {
    'device_type': 'fortinet',
    'host': '128.1.255.64',
    'username': 'admin',
    'password': 'admin',
    'secret': 'enablepass',
}

print(f"{'#' * 20} Connection to the Device {'#' * 20}")
Net_connect = Netmiko(**FW1)
print(f"{'#' * 20} Connected {'#' * 20}")

command = f'show firewall address | grep -f {search}'
output = Net_connect.send_command(command)


ip_references = ip_pattern.finditer(output)
match = False

for line in ip_references:
    print(line.group(1))
    match = True
if not match:
    print("No address Object Found")
