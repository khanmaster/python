# import requests
#
# request_bbc = requests.get("https://www.bbc.co.uk/")
# print(request_bbc.status_code)
# print(request_bbc.content)
# print(request_bbc.history)

import requests

request_bbc = requests.get("https://www.bbc.co.uk/")

print(request_bbc.status_code)

print(request_bbc.__annotations__)

