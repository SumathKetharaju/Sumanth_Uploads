import json

students_string = """
{
    "student":[
        {
        "name": "Mahesh Babu",
        "phone": "9856328659",
        "email": "MaheshBabu@gmail.com",
        "has_license": false
        },
        {
        "name": "Ram Charan",
        "phone": "9875328659",
        "email": null,
        "has_license": true
        }
    ]
        
}
"""
print("\n------------------------------------- Converting Json data to Python -------------------------------------\n")
print(f"The type of given Json String before using loads function is --> {type(students_string)}")
json_to_python_data = json.loads(students_string)
print(json_to_python_data)
print(f"The type of given Json String after using loads function is --> {type(json_to_python_data)}")
print(f"The type of given student is --> {type(json_to_python_data['student'])}")

for student_details in json_to_python_data["student"]:
    print(student_details)
    del student_details["phone"]

print("\n------------------------------------- Converting Python data to Json -------------------------------------\n")
# python_to_json_data = json.dumps(json_to_python_data)
# python_to_json_data = json.dumps(json_to_python_data, indent=2)
python_to_json_data = json.dumps(json_to_python_data, indent=2, sort_keys=True)
print(f"The type of json_to_python_data before using dumps function is --> {type(json_to_python_data)}")
print(python_to_json_data)
print(f"The type of json_to_python_data after using dumps function is --> {type(python_to_json_data)}")
