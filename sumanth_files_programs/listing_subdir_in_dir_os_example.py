import os

directory_path = ("sumanth_directory")

for sub_dir in os.listdir(directory_path):
    if os.path.isdir(os.path.join(directory_path, sub_dir)):
        print(sub_dir)

# with os.scandir(directory_path) as directories:
#     for sub_dir in directories:
#         if sub_dir.is_dir():
#             print(sub_dir.name)
