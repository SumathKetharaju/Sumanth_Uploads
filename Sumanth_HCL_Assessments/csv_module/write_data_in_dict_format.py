import csv

with open("sample_file.csv", "r") as r:
    # csv_reader = csv.reader(r)
    csv_reader = csv.DictReader(r)
    # # print(csv_reader)
    # for line in csv_reader:
    #     print(line)

    with open("sample_dict.csv", "w") as w:
        # csv_writer = csv.writer(w)
        # filed_names = ["first_name", "last_name", "gmail_id"]
        filed_names = ["first_name", "last_name"]
        csv_writer = csv.DictWriter(w, fieldnames=filed_names, delimiter="\t")

        csv_writer.writeheader()

        for line in csv_reader:
            del line["gmail_id"]
            csv_writer.writerow(line)
