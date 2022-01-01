import os
import fnmatch

"""It prints file name, if file ends with .py/txt/csv extension in particular directory"""

# for file_name in os.listdir("sumanth_directory"):
#     if file_name.endswith(".py"):
#         print(file_name)

"""It prints file name, if file ends with .py/txt/csv extension in particular directory"""

# for file_name in os.listdir("sumanth_directory"):
#     if fnmatch.fnmatch(file_name, "*.py"):
#         print(file_name)

"""It prints file name, if file starts with sumanth in particular directory"""

for file_name in os.listdir("sumanth_directory"):
    if file_name.startswith("sumanth"):
        print(file_name)

"""It prints file name, if file starts with sumanth and endswith .py/txt/csv extension in particular directory"""

# for file_name in os.listdir("sumanth_directory"):
#     if fnmatch.fnmatch(file_name, "sumanth_*.py"):
#         print(file_name)
