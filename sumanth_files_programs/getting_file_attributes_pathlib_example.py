from pathlib import Path

current_directory = Path("sumanth_directory")

for subdir_and_file in current_directory.iterdir():
    information = subdir_and_file.stat()
    print(f"{information.st_mtime}")

