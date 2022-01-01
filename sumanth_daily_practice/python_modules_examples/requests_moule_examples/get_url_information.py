import requests

geeks_for_geeks = requests.get(r"https://www.geeksforgeeks.org/python-requests-tutorial/")

print(geeks_for_geeks.url)

print(geeks_for_geeks.status_code)

print(geeks_for_geeks.ok)

# print(geeks_for_geeks.text)

# print(geeks_for_geeks.content)
#
print(geeks_for_geeks.headers)
