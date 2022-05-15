import requests
import json

url = "http://192.168.1.86/api/cYrogcQrJAv-zqaaoNjBRljNIMF3j8AQ52F-tOBC/lights/9/state"

data_on = {"on":True, "sat":254, "bri":254,"hue":5000,"ct": 500, "xy": [
            0.6792,
            0.3038
        ]}
data_off = {"on":False}

r = requests.put(url, json.dumps(data_on), timeout=5)
