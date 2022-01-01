import requests

url = r"https://www.programiz.com/python-programming/examples"

get_url = requests.get(url)

print(get_url)

print(get_url.status_code)

# print(get_url.text)

# print(get_url.content)

print(get_url.ok)

print(get_url.headers)

print(get_url.url)
