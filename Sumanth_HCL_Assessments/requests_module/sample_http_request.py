import requests

geeks_for_geeks = requests.get(r"https://www.geeksforgeeks.org/python-requests-tutorial/")

print(f"URL of the geeks_for_geeks Response is --> {geeks_for_geeks.url}\n")

print(f"This is geeks_for_geeks Response --> {geeks_for_geeks}\n")

print(f"Status code of the geeks_for_geeks Response --> {geeks_for_geeks.status_code}\n")

print(f"This is geeks_for_geeks Exact Response --> {geeks_for_geeks.ok}\n")

# print(f"Text of the geeks_for_geeks Response is --> {sample_image.text}")

# print(f"Content of the geeks_for_geeks Response is --> {sample_image.content}")

print(f"Headers of the geeks_for_geeks Response is --> {geeks_for_geeks.headers}\n")

print(f"server of the Given URl is --> {geeks_for_geeks.headers['Server']}\n")

print(f"Content type of the Given URl is --> {geeks_for_geeks.headers['Content-Type']}\n")

print(f"Content Length of the Given URl is --> {geeks_for_geeks.headers['Content-Length']}\n")
