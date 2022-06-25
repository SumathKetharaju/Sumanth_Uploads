"""
# we can use subprocess.run function to run an external program from our python code
# subprocess.run is given a list of strings consisting of the components of the commands we are trying to run
# subprocess.run returns a subprocess.completedprocess object that is bound to result
# If we want to capture the output we will be giving keyword arguments like capture_output=True,
# By default the output is in binary if we want to convert those as string we need use command like text=True
"""

"""
subprocess.run returns a subprocess.CompletedProcess object that is bound to result. The subprocess.CompletedProcess 
object includes details about the external program’s exit code and its output. capture_output=True ensures that result.
stdout and result.stderr are filled in with the corresponding output from the external program. 
By default, result.stdout and result.stderr are bound as bytes, but the text=True keyword argument instructs 
Python to instead decode the bytes into strings.
"""

import subprocess
import sys

# sys.executable is the absolute path to the Python executable that our program was originally invoked with
# subprocess.run is given a list of strings consisting of the components of the command we are trying to run

# It runs another program then automatically gives the output of another program
# and it does not capture the output into a variable
# sp = subprocess.run([sys.executable, "to_know_available_seats.py"])

# It runs another program then automatically gives the output of another program and
# it does not capture the output into a variable
# sp = subprocess.run([sys.executable, "to_know_available_seats.py"], shell=True)

# If you want to capture the output we need use capture_output=True,and it returns output and error separately in binary
# sp = subprocess.run([sys.executable, "to_know_available_seats.py"], shell=True, capture_output=True)

# If you want to capture output in string format we need use text=True
sp = subprocess.run([sys.executable, "to_know_available_seats.py"], shell=True, capture_output=True, text=True)

# sys.executable is the absolute path to the Python executable that our program was originally invoked with
# print(sys.executable)

# subprocess.run returns a subprocess.completedprocess object that is bound to result
# print(sp)
# print("program output -->", sp.stdout)
# print("program error -->", sp.stderr)

# The -c component is a python command line option that allows you to pass a string with an
# entire Python program to execute
os_result = subprocess.run([sys.executable, "-c", "import os; print(os.listdir())"], capture_output=True, text=True)
print("os_result output --->", os_result.stdout)
#
sample_result = subprocess.run([sys.executable, "-c",
"from Sumanth_HCL_Assessments; import Assessments; print(while_loop_example_2.py.limited_dharshan_tickets)"], capture_output=True, text=True)
print("sample_result output --->", sample_result.stdout)

# python_check = subprocess.run()


