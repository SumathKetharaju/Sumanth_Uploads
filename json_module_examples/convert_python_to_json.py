import json

State_details = {"C.M": "Jagan", "H.M": "Sucharitha"}

python_to_json = json.dumps(State_details, indent=2)

print(python_to_json)
