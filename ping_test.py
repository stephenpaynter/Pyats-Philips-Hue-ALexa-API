import os
hostname = "192.168.2.254." #example
response = os.system("ping -c 1 " + hostname)
if response == 0:
    print (hostname + "is up")
else:
    print (hostname + "is down")
