import os

csv_files = []
txt_files = []

for files in os.listdir():
    if files.endswith(".csv"):
        csv_file_name = files.split(".csv")
        # print(csv_file_name)
        csv_files.append(csv_file_name[0])

    elif files.endswith(".txt"):
        txt_file_name = files.split(".txt")
        # print(csv_file_name)
        txt_files.append(txt_file_name[0])

print(f"All CSV files --> {csv_files}")
print(f"All text files --> {txt_files}")


final_result = [file for file in csv_files if file in txt_files]
print(f"Common file names from both csv and text files are --> {final_result}")
