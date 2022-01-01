from pathlib import Path

directory_path = Path("C:\\Users\\SUMANTH\\Desktop\\sumanth_files_programs\\sudheer_directory\\sudheer_age_dir")

try:
    directory_path.rmdir()
except OSError as e:
    print(f"Error: {directory_path} : {e.strerror}")
