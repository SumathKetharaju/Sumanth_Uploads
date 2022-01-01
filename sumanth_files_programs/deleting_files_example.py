import os

# file_path = "C:\\Users\\SUMANTH\\Desktop\\sumanth_files_programs\\sumanth_directory\\sumanth_personality.py"

# file_path = "C:\\Users\\SUMANTH\\Desktop\\sumanth_files_programs\\sumanth_directory\\sumanth_credentials.csv"

file_name = "C:\\Users\\SUMANTH\\Desktop\\sumanth_files_programs\\sumanth_directory\\sumanth_credentials.csv"

# os.remove(file_path)

#os.unlink(file_path)

# if os.path.isfile(file_name):
#     os.remove(file_name)
# else:
#     print(f"Error: {file_name} not valid filename")

try:
    os.remove(file_name)
except OSError as e:
    print(f"Error: {file_name} : {e.strerror}")
