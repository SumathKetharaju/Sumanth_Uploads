import requests
import json

url_ifo = requests.get("https://www.programiz.com/python-programming")

print(url_ifo)
print(url_ifo.url)
print(url_ifo.status_code)
# print(url_ifo.content)
print(url_ifo.headers)


creating_json = url_ifo.headers
print(creating_json)

# 18@@
with open("creating_from_requests.json", "w") as j:
    json.dump(creating_json, j)

