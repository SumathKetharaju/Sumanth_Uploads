from pathlib import Path

list_of_current_directory = Path("sumanth_directory")

for subdir_and_file in list_of_current_directory.iterdir():
    print(subdir_and_file.name)
