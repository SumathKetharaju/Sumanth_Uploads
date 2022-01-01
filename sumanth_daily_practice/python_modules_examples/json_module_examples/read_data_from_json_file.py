import json

with open("college.json", "r") as r:
    data = json.load(r)
    print(data)
