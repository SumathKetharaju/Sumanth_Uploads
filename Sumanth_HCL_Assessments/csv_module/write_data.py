import csv

with open("sample_file.csv", "r") as f:
    csv_reader = csv.reader(f)
    # print(csv_reader)
    with open("new_file.csv", "w") as w:
        # csv_writer = csv.writer(w, delimiter="-")
        csv_writer = csv.writer(w, delimiter="\t")
        for line in csv_reader:
            csv_writer.writerow(line)

