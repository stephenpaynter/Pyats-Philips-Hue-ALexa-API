import requests
import json

response = requests.get("http://192.168.1.86/api/cYrogcQrJAv-zqaaoNjBRljNIMF3j8AQ52F-tOBC/lights")

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
