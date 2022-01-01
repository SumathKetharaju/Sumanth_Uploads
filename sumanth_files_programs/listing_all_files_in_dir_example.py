import os

directory_path = "sumanth_directory"

for file in os.listdir(directory_path):
    if os.path.isfile(os.path.join(directory_path, file)):
        print(file)

# with os.scandir(directory_path) as directories:
#     for file in directories:
#         if file.is_file():
#             print(file.name)
