import example

print(example.output)

# import subprocess
# import sys
#
# # sys.executable is the absolute path to the Python executable that our program was originally invoked with
# # subprocess.run is given a list of strings consisting of the components of the command we are trying to run
#
# # It runs another program then automatically gives the output of another program
# # and it does not capture the output into a variable
# # sp = subprocess.run([sys.executable, "to_know_available_seats.py"])
#
# # It runs another program then automatically gives the output of another program and
# # it does not capture the output into a variable
# # sp = subprocess.run([sys.executable, "to_know_available_seats.py"], shell=True)
#
# # If you want to capture the output we need use capture_output=True,and it returns output and error separately in binary
# # sp = subprocess.run([sys.executable, "to_know_available_seats.py"], shell=True, capture_output=True)
#
# # If you want to capture output in string format we need use text=True
# sp = subprocess.run([sys.executable, "test_math_func.py"], shell=True, capture_output=True, text=True)
#
# print(sp)
# print("program output -->", sp.stdout)
# print("program error -->", sp.stderr)

