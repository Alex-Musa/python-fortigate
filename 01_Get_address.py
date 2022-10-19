import requests
from pprint import pprint


# Geting Address Object

url = "http://192.168.12.152/api/v2/cmdb/firewall/address"

headers = {
  'Authorization': 'Bearer f1yH4kpGfx06h8p3h9wcfb19g9qt0H'
}

response = requests.request("GET", url, headers=headers)

pprint(response.json()['results'])