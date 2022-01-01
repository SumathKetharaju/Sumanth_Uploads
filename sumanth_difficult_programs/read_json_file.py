import json

with open("file.json", "r") as f:
    data = json.load(f)

print("This prints all the data present in json file: ")
print(data)
print()

print("This prints data present in particular key present in json file: ")
for person in data["Details"]:
    print(person)
print()

print("This prints data present in particular key present in json file:  ")
for person in data["Credentials"]:
    print(person)
print()

print("This prints data present in particular nested key present in json file: ")
for person in data["Details"]:
    print(person["Name"])
print()

print("This prints data present in particular nested key present in json file: ")
for person in data["Credentials"]:
    print(person["Father"])
