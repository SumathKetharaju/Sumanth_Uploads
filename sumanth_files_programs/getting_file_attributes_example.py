import os

with os.scandir("sumanth_directory") as current_directory:
    for subdir_and_file in current_directory:
        information = subdir_and_file.stat()
        print(information.st_mtime)
