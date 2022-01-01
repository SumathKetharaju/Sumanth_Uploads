import os


for dir_path, dir_names, files in os.walk(".", topdown=False):
    try:
        os.rmdir(dir_path)
    except OSError as e:
        pass
