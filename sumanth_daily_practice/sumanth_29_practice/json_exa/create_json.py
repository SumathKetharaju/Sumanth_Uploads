import json

creating_json = {"Name_1": "Sumanth", "Name_2": "Mahesh", "Name_3": "Bharath", "Name_4": "Avinash", "Name_5": "Visweswar"}

with open("team.json", "w") as j:
    json.dump(creating_json, j, indent=4)

with open(r"C:\Users\SUMANTH\Desktop\team.json", "w") as j:
    json.dump(creating_json, j, indent=4)