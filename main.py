import requests

payload = {'username': 'corey', "password": 'testing'}

r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))

print(r)




