import os

# Walking a directory tree and printing the names of the directories and files

print('"To traverse the directory tree in topdown manner as below: "')
print()

for dir_path, dir_names, files in os.walk("sumanth_directory"):
    print(f"Found current_directory: {dir_path}")
    for file_name in files:
        print(file_name)
    print()

# To traverse the directory tree in a bottom-up manner, pass in a topdown=False keyword argument to os.walk()

print('"To traverse the directory tree in a bottom-up manner as below: "')
print()

for dir_path, dir_names, files in os.walk("sumanth_directory", topdown=False):
    print(f"Found current_directory: {dir_path}")
    for file_name in files:
        print(file_name)
    print()
