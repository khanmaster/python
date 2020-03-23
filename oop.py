# # Object oriented programming
# print("OOP object oriented programming")

import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))