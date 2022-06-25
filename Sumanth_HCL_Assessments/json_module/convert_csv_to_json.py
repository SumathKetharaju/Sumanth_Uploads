import csv
import json

csv_file_path = r'C:\Users\SUMANTH\Desktop\Sumanth_HCL_Assessments\csv_module\sample_file.csv'
json_file_path = r'C:\Users\SUMANTH\Desktop\Sumanth_HCL_Assessments\json_module\current_file.json'


def make_json(csv_file_path, json_file_path):
    data = {}

    with open(csv_file_path, encoding='utf-8') as r:
        csv_reader = csv.DictReader(r)

        for rows in csv_reader:
            key = rows["first_name"]
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


make_json(csv_file_path, json_file_path)

