import csv

with open("sample_file.csv", "r") as r:
    # csv_reader = csv.reader(r)
    csv_reader = csv.DictReader(r, skipinitialspace=True)
    # csv_reader = csv.DictReader(r, delimiter="\t")
    print(csv_reader)
    for line in csv_reader:
        print(line)
        # print(dict(line))
        # print(line['gmail_id'])
    print(f"Type of line is {type(line)}")


"""
<csv.DictReader object at 0x0000021451EB7E20>
{'first_name': 'Sumanth', 'last_name': 'Ketharaju', 'gmail_id': 'SumanthKetharaju@gmail.com'}
{'first_name': 'Ravindra', 'last_name': 'Ketharaju', 'gmail_id': 'SumanthKetharaju@gmail.com'}
{'first_name': 'Sunil', 'last_name': 'Pamujula', 'gmail_id': 'SunilPamujula@gmail.com'}
{'first_name': 'Sudheer', 'last_name': 'Pamujula', 'gmail_id': 'SudheerPamujula@gmail.com'}
{'first_name': 'Seshu', 'last_name': 'Byna', 'gmail_id': 'SeshuByna@gmail.com'}
Type of line is <class 'dict'>
"""
