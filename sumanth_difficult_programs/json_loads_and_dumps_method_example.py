import json

sample_string = """
{
  "Details": [
    {
      "Name": "Sumanth",
      "Age": 24,
      "Behavior": "Not bad",
      "Location": false,
      "Role": "Test Engineer"
    },
    {
      "Name": "Sunil",
      "Age": 22,
      "Behavior": "Not bad",
      "Location": true,
      "Role": null
    }
  ]
}
"""
print("This prints type of what you want to enter before convert it into json to python: ")
print(type(sample_string))
print(type("Details"))
print()

print("This prints all the data present in sample_string after convert it into json to python: ")
data = json.loads(sample_string)
print(data)
print()

print("This prints type of what you want to enter after convert it into json to python: ")
print(type(data))
print(type(data["Details"]))
print()

print("This prints data present in particular key present in sample_string: ")
for name in data["Details"]:
    print(name)
print()

print("This prints data present in particular nested key present in sample_string: ")
for name in data["Details"]:
    print(name["Name"])
print()

print("This prints all the data present in sample_string after convert it into python to json: ")
new_string = json.dumps(data, indent=4)
print(new_string)
