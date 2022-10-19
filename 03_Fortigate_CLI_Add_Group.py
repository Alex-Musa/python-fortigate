from csv import DictReader
import time
from netmiko import Netmiko

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


with open('01_IP_List_Group.csv') as csv_file:
    ip_details = DictReader(csv_file)
    time.sleep(2)

    for ip in ip_details:
        time.sleep(2)
        print(f"{'#' * 20} Configuring Object {ip['Name']} {'#' * 20}")

        config = ['config firewall address',
                  f'edit {ip["Name"]}',
                  f'set subnet {ip["IP"]}',
                  'end',
                  'config firewall addrgrp',
                  f'edit {ip["Group"]}',
                  f'append member {ip["Name"]}',
                  'end'
                  ]

        send_config = Net_connect.send_config_set(config)
        print(send_config)