
import requests

endpoint = 'https://api.eu.amazonalexa.com/v1/alerts/alarms?endpointId=<serial_number>@<device_id>'
#device_id can be found by editing the alarm within alexa.com website

headers = {'Authorization' : 'Bearer <bearer_token>
print (requests.get(endpoint, headers=headers).json())
