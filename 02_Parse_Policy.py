from re import I
import requests

url = "http://128.1.255.64/api/v2/cmdb/firewall/policy"

payload={}
headers = {
  'Authorization': 'Bearer dqhdm433ckN8w08tt8N3xGk6nxp7xy'
}

response = requests.request("GET", url, headers=headers, data=payload)

results = response.json()['results']
total = len(results)


for i in range(0,total):
    print(f"\n\n{'Policy Name:'.ljust(15)}{results[i]['name']}")
    print(f"{'Source Int:'.ljust(15)}{results[i]['srcintf'][0]['name']}")
    print(f"{'Destination Int:'.ljust(15)}{results[i]['dstintf'][0]['name']}")
    print(f"{'Service:'.ljust(15)}{results[i]['service'][0]['name']}")
    print(f"{'Action:'.ljust(15)}{results[i]['action']}")







