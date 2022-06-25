import requests

# sample_image = requests.get("https://all-free-download.com/free-photos/download/iphone_6_sample_photo_566464.html")
sample_image = requests.get("https://www.fnordware.com/superpng/pnggrad16rgb.png")

print(f"URL of the Sample Image Response is --> {sample_image.url}")

print(f"This is Sample Image Response --> {sample_image}")

print(f"Status code of the Sample Image Response --> {sample_image.status_code}")

print(f"This is Sample Image Exact Response --> {sample_image.ok}")

# print(f"Text of the Sample Image Response is --> {sample_image.text}")

# print(f"Content of the Sample Image Response is --> {sample_image.content}")

print(f"Headers of the Sample Image Response is --> {sample_image.headers}")

print(f"server of the Given URl is --> {sample_image.headers['Server']}")

print(f"Content type of the Given URl is --> {sample_image.headers['Content-Type']}")

print(f"Content Length of the Given URl is --> {sample_image.headers['Content-Length']}")

# with open(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\sample_color_image.png", "wb") as f:
#     f.write(sample_image.content)

# with open(r"C:\Users\SUMANTH\Desktop\Automation_Purposes\Automations\sample_nature_image.jpg", "wb") as f:
#     f.write(sample_image.content)

