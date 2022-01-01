import os

# print(os.listdir())

for sub_dir_or_file in os.listdir():
    if os.path.isfile(sub_dir_or_file):
        print(sub_dir_or_file)
