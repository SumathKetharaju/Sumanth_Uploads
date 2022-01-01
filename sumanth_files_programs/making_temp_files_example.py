import os
import tempfile
from tempfile import TemporaryFile

# temp_file = TemporaryFile("w+t")
#
# temp_file.write("Hello sumanth")
#
# temp_file.seek(0)
#
# information = temp_file.read()
#
# temp_file.close()

# with TemporaryFile("w+t") as temp_file:
#     temp_file.write("How are you")
#     temp_file.seek(0)
#     temp_file.read()

with tempfile.TemporaryDirectory() as temp_dir:
    print("Newly created temperary directory", temp_dir)
    os.path.exists(temp_dir)
