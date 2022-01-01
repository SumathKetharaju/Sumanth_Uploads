import shutil

directory_path = "C:\\Users\\SUMANTH\\Desktop\\sumanth_files_programs\\seshu_directory"

try:
    shutil.rmtree(directory_path)
except OSError as e:
    print(f"Error: {directory_path} : {e.strerror}")
