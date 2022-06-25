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
print("---------------------------------------------------------------------------------------------------------------")
print(f"The absolute path to the Python executable that our program was originally invoked with is --> {sys.executable}\n")

print("------------------------------------ String_operations Program ---------------------------------------------\n")
# It runs another program then automatically gives the output of another program
# and it does not capture the output into a variable
run_string_operations_program = subprocess.run([sys.executable, "string_operations.py"])

# subprocess.run returns a subprocess.completedprocess object that is bound to result
print(run_string_operations_program)
print("string_operations.py program output -->", run_string_operations_program.stdout)
print("string_operations.py program error -->", run_string_operations_program.stderr)
print("-------------------------------------------------------------------------------------------------------------\n")


print("------------------------------------ Duplicate_characters Program ------------------------------------------\n")
# It runs another program then automatically gives the output of another program and
# it does not capture the output into a variable
run_duplicate_characters_program = subprocess.run([sys.executable, "duplicate_characters.py"], shell=True)
# subprocess.run returns a subprocess.completedprocess object that is bound to result
print(run_duplicate_characters_program)
print("duplicate_characters.py program output -->", run_duplicate_characters_program.stdout)
print("duplicate_characters.py program error -->", run_duplicate_characters_program.stderr)
print("-------------------------------------------------------------------------------------------------------------\n")

print("----------------------- Duplicate_characters Program with output as binary --------------------------------\n")

# If you want to capture the output we need use capture_output=True,and it returns output and error separately in binary
run_duplicate_characters_with_output_in_bin = subprocess.run([sys.executable, "duplicate_characters.py"],
                                                             shell=True, capture_output=True)

# subprocess.run returns a subprocess.completedprocess object that is bound to result
print(f"{run_duplicate_characters_with_output_in_bin}\n")
print(f"duplicate_characters.py program output --> {run_duplicate_characters_with_output_in_bin.stdout}\n")
print(f"duplicate_characters.py program error --> {run_duplicate_characters_with_output_in_bin.stderr}\n")
print("-------------------------------------------------------------------------------------------------------------\n")

print("----------------------- Duplicate_characters Program with output as String --------------------------------\n")
# If you want to capture output in string format we need use text=True
run_duplicate_characters_with_output_in_str = subprocess.run([sys.executable, "duplicate_characters.py"],
                                                             shell=True, capture_output=True, text=True)

# subprocess.run returns a subprocess.completedprocess object that is bound to result
print(f"{run_duplicate_characters_with_output_in_str}\n")
print(f"duplicate_characters.py program output --> {run_duplicate_characters_with_output_in_str.stdout}\n")
print(f"duplicate_characters.py program error --> {run_duplicate_characters_with_output_in_str.stderr}\n")
print("-------------------------------------------------------------------------------------------------------------\n")

