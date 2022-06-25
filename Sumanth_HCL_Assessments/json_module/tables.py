import json
import os


current_file_name = os.path.basename(__file__)
print(current_file_name)
current_file_name = current_file_name.split(".")
print(current_file_name)
current_json = current_file_name[0]+".json"

for files in os.listdir():
    if current_json in files:
        with open(current_json, "r") as j:
            data = json.load(j)
            print(data)
            for index in range(len(data["input"])):
                for i in range(1, 11):
                    num = (data["input"][index])
                    print(f"{num} * {i} = {num * i}")
                print()
    else:
        pass


