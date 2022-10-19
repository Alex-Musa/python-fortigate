from csv import DictReader
import time
from netmiko import Netmiko

#------------------ SSH to Devices ------------------------------------------------------
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

#------------------  END SSH to Devices ------------------------------------------------------

#------------------  Open CSV File ------------------------------------------------------
with open('01_IP_List.csv') as csv_file:
    ip_details = DictReader(csv_file)

#------------------  Loop throu CSV File and Push configation  ------------------------------------------------------
    for ip in ip_details:
        time.sleep(2)
        print(f"{'#' * 20} Configuring Object {ip['Name']} {'#' * 20}")

        config = ['config firewall address',
                  f'edit {ip["Name"]}',
                  f'set subnet {ip["IP"]}',
                  'end'
                  ]
        send_config = Net_connect.send_config_set(config)
        print(send_config)


