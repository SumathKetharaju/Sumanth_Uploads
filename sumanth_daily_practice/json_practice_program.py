import json

college_data = """
{
"college_name" : "Gist",
"Address" : "Kovur"
}
"""

json_to_python = json.loads(college_data)

print(type(college_data))
print(json_to_python)
print(type(json_to_python))

python_to_json = json.dumps(json_to_python, indent=4)
print(python_to_json)
print(type(python_to_json))

with open("college_data.json", "w") as f:
    json.dump(json_to_python, f, indent=2, sort_keys=True)

with open("college_data.json", "r") as r:
    print(json.load(r))
