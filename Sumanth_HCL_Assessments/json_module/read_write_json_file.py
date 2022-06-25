import json

print("\n-------------------------------  Reading the data from Json file -----------------------------------------\n")
with open("sample_file.json", "r") as f:
    sample_json_data = json.load(f)
    print(f"The data Present in the sample_file.json is --> {sample_json_data}")
    print(f"The type of given Json String after using load function is --> {type(sample_json_data)}")

for student_details in sample_json_data["student"]:
    print(student_details)
    del student_details["phone"]

print("\n--------------------- Writing the Json data to new Json file after doing some changes ---------------------\n")
print(f"The data Present in the sample_file.json after deleting phone number is --> {sample_json_data}")
with open("new_file.json", "w") as w:
    json.dump(sample_json_data, w, indent=2)
