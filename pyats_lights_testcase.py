from genie.conf import Genie
from genie.utils import Dq
from genie.testbed import load
import requests
import json

url = "http://192.168.1.86/api/cYrogcQrJAv-zqaaoNjBRljNIMF3j8AQ52F-tOBC/lights/9/state"

_data_on_red = {"on":True, "sat":254, "bri":254,"hue":5000,"ct": 500, "xy": [0.6792, 0.3038]}
_data_on_green = {"on":True, "sat":254, "bri":254,"hue":5000,"ct": 500, "xy": [0.2688, 0.6171]}

_testbed = load('/Repositories/1-Ansible Code/testbed.yml') 
_device = _testbed.devices['R1']
_device.connect()
_routes = _device.parse('show ip route') 

print(_routes)

_routecheck = len(_routes['vrf']['default']['address_family']['ipv4']['routes']) 

print (_routecheck)

if _routecheck == 6:
   r = requests.put(url, json.dumps(_data_on_green), timeout=5)
elif _routecheck != 6:
   r = requests.put(url, json.dumps(_data_on_red), timeout=5)
