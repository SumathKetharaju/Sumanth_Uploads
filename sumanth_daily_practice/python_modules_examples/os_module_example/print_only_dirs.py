import os

for sub_dir_or_file in os.listdir():
    if os.path.isdir(sub_dir_or_file):
        print(sub_dir_or_file)
