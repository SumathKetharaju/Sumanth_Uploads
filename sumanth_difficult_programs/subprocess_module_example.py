import subprocess

# This prints all the files present in the current directory with date and time:
# subprocess.run("dir", shell=True)

# p1 = subprocess.run("dir", shell=True)
# This prints all the files present in the current directory with date and time and also with completedprocess
# print(p1)

# This prints args:
# print(p1.args)
#
# This prints whether it is run success(0) or failure(1):
# print(p1.returncode)
#
# print("This prints None")
# print(p1.stdout)

# This prints all the files present in the current directory with date and time in binary format
# p1 = subprocess.run("dir", shell=True, capture_output=True)
# print(p1.stdout)

# This prints all the files present in the current directory with date and time in normal format
# print(p1.stdout.decode())

# This also prints all the files present in the current directory with date and time in binary format
# p1 = subprocess.run("dir", shell=True, stdout=subprocess.PIPE)
# print(p1.stdout)

# This prints all the files present in the current directory with date and time in normal format
# p1 = subprocess.run("dir", shell=True, stdout=subprocess.PIPE, text=True)
# print(p1.stdout)

# This creates a text file and prints all the files present in the current directory with date & time in normal format
# with open("output.txt", "w") as f:
#     p1 = subprocess.run("dir", shell=True, stdout=f)

p1 = subprocess.run("dir", shell=True, stdout=subprocess.PIPE, text=True)
print(p1.stderr)

# p1 = subprocess.run("dir", shell=True, stderr=subprocess.DEVNULL)
# print(p1.stderr)

# p1 = subprocess.run("dir", shell=True, stderr=subprocess.DEVNULL, text=True, check=True)
# print(p1.stderr)
