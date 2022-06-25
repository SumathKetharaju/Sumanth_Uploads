import csv

with open("new_file.csv", "r") as f:
    csv_reader = csv.reader(f)
    csv_reader_2 = csv.reader(f, delimiter="\t")
    print(csv_reader)
    # for line in csv_reader:
    #     print(line)
        # print(line[0])
        # print(line[2])
    for line_2 in csv_reader_2:
        print(line_2)


"""
<_csv.reader object at 0x000001AC35E4ECA0>
['first_name', 'last_name', 'gmail_id']
['Sumanth', 'Ketharaju', 'SumanthKetharaju@gmail.com']
['Ravindra', 'Ketharaju', 'SumanthKetharaju@gmail.com']
['Sunil', 'Pamujula', 'SunilPamujula@gmail.com']
['Sudheer', 'Pamujula', 'SudheerPamujula@gmail.com']
['Seshu', 'Byna', 'SeshuByna@gmail.com']
Type of line is <class 'list'>
"""
