import os

# directory_path = "C:\\Users\\SUMANTH\\Desktop\\sumanth_files_programs\\sudheer_directory\\sudheer_age_dir\\sudheer_colour_dir"
#
# try:
#     os.rmdir(directory_path)
# except OSError as e:
#     print(f"Error: {directory_path} : {e.strerror}")


directory_path2 = "C:\\Users\\SUMANTH\\Desktop\\sumanth_files_programs\\sudheer_directory"

try:
    os.rmdir(directory_path2)
except OSError as e:
    print(f"Error: {directory_path2} : {e.strerror}")

