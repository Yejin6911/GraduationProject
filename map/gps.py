import json
import requests

# url = 'http://18.180.217.31:8080/Alert/'
url = 'http://127.0.0.1:8000/Alert/'
# url = 'http://32bb5c34a862.ngrok.io/Alert/'

client = requests.session()
client.get(url)
print(client)
cookies = client.cookies
print(cookies)
#csrftoken = client.cookies['csrftoken']
# if 'csrftoken' in client.cookies:
#     # Django 1.6 and up
#     csrftoken = client.cookies['csrftoken']
# else:
#     # older versions
#     csrftoken = client.cookies['csrf']
#
# print(csrftoken)
data = {
    'latitude': 37.5616185,
    'longitude': 126.9437005,
    #'csrfmiddlewaretoken': csrftoken,
}
data = json.dumps(data)

headers = {'Content-Type': 'application/json' }
r = requests.post(url, headers=headers, data=data)
