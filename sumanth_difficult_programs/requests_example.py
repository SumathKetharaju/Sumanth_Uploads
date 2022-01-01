import requests

# python_tutorial = requests.get(r"https://www.programiz.com/python-programming")
# print("It prints the response:  ")
# print(python_tutorial)

# print("dir function shows the attributes and methods that we can access from particular response: ")
# print(dir(python_tutorial))
# print()

# print("help function shows the information about attributes and methods that we can access from particular response:")
# print(help(python_tutorial))
# print()

# print("This shows content of the response in unicode: ")
# print(python_tutorial.text)


sample_image = requests.get("https://cdn.programiz.com/sites/tutorial2program/files/forLoop.jpg")

# print("This prints content of the image in binary format: ")
# print(sample_image.content)

# print("This prints status code of the sample_image: ")
# print(sample_image.status_code)

# print("This prints status code of the sample_image is True or false: ")
# print(sample_image.ok)


# print("This creates a file i.e sample.jpeg and print the image in that file")
# with open("sample.jpeg", "wb") as write_to_file:
#     write_to_file.write(sample_image.content)

print("This prints headers of the sample_image: ")
print(sample_image.headers)
