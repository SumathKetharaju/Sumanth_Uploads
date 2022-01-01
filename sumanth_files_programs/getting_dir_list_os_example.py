# Getting list of directories using os module
#
import os
# list_of_current_directory = os.listdir("sumanth_directory")
# print(list_of_current_directory)

# Getting list of directories using os module by for loop
list_of_current_directory = os.listdir("sumanth_directory")
for subdir_and_file in list_of_current_directory:
    print(subdir_and_file)

# list_of_current_directory = os.scandir("sumanth_directory")
# print(list_of_current_directory)

# with os.scandir("sumanth_directory") as list_of_current_directory:
#     for subdir_and_file in list_of_current_directory:
#         print(subdir_and_file.name)
