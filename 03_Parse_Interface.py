import requests
import csv
import pdb

url = "http://192.168.12.152/api/v2/cmdb/system/interface/"

headers = {'Authorization': 'Bearer dqhdm433ckN8w08tt8N3xGk6nxp7xy'}

response = requests.request("GET", url, headers=headers)

results = response.json()['results']
total = len(results)
#pdb.set_trace()


# Loop through all the Fortigate firewall to get Interface status
print("\n######### Current Query Interface Status ###########\n")

for i in range(0,total):
    print(f"\n\n{'Interface'.ljust(15)}{results[i]['name']}")
    print(f"{'description'.ljust(15)}{results[i]['description']}")
    print(f"{'IP'.ljust(15)}{results[i]['ip']}")
    print(f"{'inbandwidth'.ljust(15)}{results[i]['inbandwidth']}")
    print(f"{'outbandwidth'.ljust(15)}{results[i]['outbandwidth']}")

data_list = []

for line in results:
    data_list.append({"Interface":line['name'], 
                      "description": line["description"], 
                      "IP": line["ip"], 
                      "inbandwidth": line["inbandwidth"], 
                      "outbandwidth":line["outbandwidth"]})

keys = data_list[0].keys()

with open('netcom.csv', 'w') as f:
        #pdb.set_trace()
    w = csv.DictWriter(f, keys)
    w.writeheader()
    w.writerows(data_list)