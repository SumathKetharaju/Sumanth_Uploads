# listing all files in directory using generator expression by pathlib module
from pathlib import Path

directory_path = Path("sumanth_directory")
#
files_in_directory_path = directory_path.iterdir()
#
for file in files_in_directory_path:
    if file.is_file():
        print(file.name)

# listing all files in directory using generator expression by pathlib module

# directory_path = Path("sumanth_directory")
#
# files_in_directory_path = (file for file in directory_path.iterdir() if file.is_file())
#
# for file in files_in_directory_path:
#     print(file.name)
