import json

college_details = {"Name": "GIST", "Principal": "Subbarao", "Correspondent": "Srinivasulu", "Address": "Kovur"}

with open("sample.json", "w") as w:
    json.dump(college_details, w, indent=4)
