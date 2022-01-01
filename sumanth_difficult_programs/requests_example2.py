import requests

# payload = {"page": 2, "count": 25}
# info = requests.get("https://httpbin.org/get", params=payload)

# print(info)
# print(info.text)
# print(info.url)

# print("this method updates the information")
# print(" in this case The method is not allowed for the requested URL.</p> because it not allows outsiders ")
# payload = {"username": "mahesh", "password": "example"}
# info = requests.post("https://httpbin.org/get", data=payload)

# print(info.text)

# info_dict = info.json()

# print(info.json())

# print(info_dict["args"])

# auth_info = requests.post("https://httpbin.org/basic-auth/mahesh/example", auth=("mahesh", "example"))
# print(auth_info)

time_out_info = requests.post("https://httpbin.org/delay/6", timeout=10)
print(time_out_info)
