import json
import requests

bodypass = json.dumps({
 "notification": "Hello World",
 "accessCode": "amzn1.ask.account.AEDNYHP3724A4XZEYNKSUJLB2FL2EWO6D7AI6JAZEJFQYBTYVY2GJP4E567VUXDVCWVTMQKSTO727Y22DD66VECXC5TZG6QPNHJ5RQR3U4MALNEMGSKDFGVN2RZP2VCGY46WQ5KTRYKOFPAF5J5JNRBTHGFBCUB7SNPBNK7DRLEXLBQJJSSOMYAUQSXVWT6JXPSLMUXFK2JXE5Y"
})


requests.post(url = "https://api.notifymyecho.com/v1/NotifyMe", data = bodypass)