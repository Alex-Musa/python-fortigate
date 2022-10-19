from netmiko import Netmiko

search = input("Enter Object Name : ")

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

command = f'diagnose sys cmdb refcnt show firewall.address:name {search}'
output = Net_connect.send_command(command)

match = False

if output :
    match = True
    print(output)
else:
    print("No refernce found")