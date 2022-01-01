from pathlib import Path

file_path = Path("C:\\Users\\SUMANTH\\Desktop\\sumanth_files_programs\\sumanth_directory\\sumanth_height.py")

try:
    file_path.unlink()
except IsADirectoryError as e:
    print(f"Error: {file_path} : {e.strerror}")

