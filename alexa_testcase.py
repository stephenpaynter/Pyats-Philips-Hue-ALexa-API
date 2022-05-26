from genie.conf import Genie
from genie.utils import Dq
from genie.testbed import load
import requests
import json

bodypass = json.dumps({
 "notification": "Route validation passed",
 "accessCode": "amzn1.ask.account.AEDNYHP3724A4XZEYNKSUJLB2FL2EWO6D7AI6JAZEJFQYBTYVY2GJP4E567VUXDVCWVTMQKSTO727Y22DD66VECXC5TZG6QPNHJ5RQR3U4MALNEMGSKDFGVN2RZP2VCGY46WQ5KTRYKOFPAF5J5JNRBTHGFBCUB7SNPBNK7DRLEXLBQJJSSOMYAUQSXVWT6JXPSLMUXFK2JXE5Y"
})

bodyfail = json.dumps({
 "notification": "Route validation failed",
 "accessCode": "amzn1.ask.account.AEDNYHP3724A4XZEYNKSUJLB2FL2EWO6D7AI6JAZEJFQYBTYVY2GJP4E567VUXDVCWVTMQKSTO727Y22DD66VECXC5TZG6QPNHJ5RQR3U4MALNEMGSKDFGVN2RZP2VCGY46WQ5KTRYKOFPAF5J5JNRBTHGFBCUB7SNPBNK7DRLEXLBQJJSSOMYAUQSXVWT6JXPSLMUXFK2JXE5Y"
})

_testbed = load('/Repositories/1-Ansible Code/testbed.yml') 
_device = _testbed.devices['R1']
_device.connect()
_routes = _device.parse('show ip route') 

print(_routes)


_routecheck = len(_routes['vrf']['default']['address_family']['ipv4']['routes']) 

print (_routecheck)

if _routecheck == 6:
   r = requests.post(url = "https://api.notifymyecho.com/v1/NotifyMe", data = bodypass)
else:
   r = requests.post(url = "https://api.notifymyecho.com/v1/NotifyMe", data = bodyfail)
