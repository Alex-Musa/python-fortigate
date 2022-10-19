from netmiko import Netmiko
import csv

# Global variables
result_list = []

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
#print(Net_connect.find_prompt())

#This block of code will do show full-configuration command show print out on CLI
command = 'show full-configuration'
full_config = Net_connect.send_command(command)
print(full_config)

# Push confong
config = ['config firewall address',
         'edit IP_101',
         'set subnet 192.168.1.101/24',
         'end'
         ]
# This code will send the list(config)
send_config = Net_connect.send_config_set(config)
print(send_config)

full_config_words = []
full_config_lines = full_config.split("\n")
for line in full_config_lines:
    temp_list = line.split(" ")
    for word in temp_list:
        if word != '':
            full_config_words.append(word)
print("\n######### Writing Output to File ###########\n")
print(full_config_words)
#print (f'Writing to file {full_config_words}')

# Write output to CSV file
with open('Lynden_Site.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, full_config)
    dict_writer.writeheader()
    dict_writer.writerows(result_list)


