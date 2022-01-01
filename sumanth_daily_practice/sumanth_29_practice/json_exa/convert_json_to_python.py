import json

json_string = """
{   "Name_1" : "Sumanth",
    "Name_2" : "Mahesh",
    "Name_3" : "Bharath",
    "Name_4" : "Avinash",
    "Name_5" : "Visweswar"
}
"""

convert_json_to_python = json.loads(json_string)
print(convert_json_to_python)
