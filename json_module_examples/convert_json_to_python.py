import json

villege_details = """
{
"Name" : "Buchireddypalem",
"Street" : "Kasipalem", 
"comminssioner" : "Srinivasulu"
}
"""

json_to_python = json.loads(villege_details)
print(json_to_python)
