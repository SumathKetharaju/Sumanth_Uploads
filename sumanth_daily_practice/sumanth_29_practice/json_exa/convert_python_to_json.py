import json

python_obj = {"Name": "Sumanth", "Age": "26"}

convert_python_to_json = json.dumps(python_obj, indent=4)

print(convert_python_to_json)
