import requests
import json

r = requests.get('http://192.168.1.86/api/cYrogcQrJAv-zqaaoNjBRljNIMF3j8AQ52F-tOBC/lights/8/')
print (r.content)
