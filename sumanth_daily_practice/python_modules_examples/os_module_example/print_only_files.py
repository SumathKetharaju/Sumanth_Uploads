import os

for files in os.listdir():
    if os.path.isfile(files):
        print(files)
