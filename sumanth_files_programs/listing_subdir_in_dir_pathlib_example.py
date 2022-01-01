from pathlib import Path

directory_path = Path("sumanth_directory")

for sub_dir in directory_path.iterdir():
    if sub_dir.is_dir():
        print(sub_dir.name)
