# If the path already exists, mkdir() raises a FileExistsError


from pathlib import Path

same_directory = Path("ravindra_directory")

same_directory.mkdir()

# To avoid errors like this, catch the error when it happens and let your user know

# same_directory = Path("ravindra_directory")
#
# try:
#     same_directory.mkdir()
# except FileExistsError as exe:
#     print(exe)


# Alternatively, you can ignore the FileExistsError by passing the exist_ok=True argument to .mkdir()

# same_directory = Path("ravindra_directory")

# same_directory.mkdir(exist_ok=True)
