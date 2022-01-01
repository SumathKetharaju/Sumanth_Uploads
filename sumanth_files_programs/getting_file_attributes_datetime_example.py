from datetime import datetime

from os import scandir


def convert_date(timestamp):

    date = datetime.utcfromtimestamp(timestamp)
    formated_date = date.strftime("%d %b %y")
    return formated_date

def get_files():
    current_directory = scandir("sumanth_directory")
    for file in current_directory:
        if file.is_file():
            information = file.stat()
            print(f"{file.name} \tLast Mpdified: {convert_date(information.st_mtime)}")


get_files()
