import requests

functions = requests.get("https://www.programiz.com/python-programming/list")

print(f"URL of the function is --> {functions.url}")

print(f"Type of function URL is --> {type(functions.url)}")

print(f"function Response is --> {functions}")

print(f"Type of function Response is --> {type(functions)}")

print(f"Status code of the function--> {functions.status_code}")

print(f"Type of Status code of  the function Response is --> {type(functions.status_code)}")

print(f"This is function Exact Response --> {functions.ok}")

print(f"Type of function Exact Response is --> {type(functions.ok)}")

# print(f"Text of the function is --> {functions.text}")

# print(f"Content of the function is --> {functions.content}")

print(f"Headers of the function Response is --> {functions.headers}")

print(f"Type of Headers of the function Response is --> {type(functions.headers)}")

print(f"server of the Given URl is --> {functions.headers['server']}")
