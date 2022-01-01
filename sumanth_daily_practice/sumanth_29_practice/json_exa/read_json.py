import json

with open("team.json", "r") as j:
    reading_json = json.load(j)
    print(reading_json)

with open(r"C:\Users\SUMANTH\Desktop\team.json", "r") as j:
    reading_json = json.load(j)
    print(reading_json)
