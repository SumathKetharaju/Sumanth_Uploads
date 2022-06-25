import subprocess

print("--------------------------------------------- subprocess ------------------------------------------------------")
print("--------------------------------------------- host name ------------------------------------------------------")

cmd = "ipconfig"

# if you run this the output would be in binary
# know_ip_address = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# so we need to use universal_newlines=True to get the output as string
# know_ip_address = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

know_ip_address = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
know_ip_address.wait()

return_code = know_ip_address.wait()
output, error = know_ip_address.communicate()

print(f"Return code of ip_address is --> {return_code}\n")
print(f"Output of ip_address is --> \n{output}\n")
print(f"Error of ip_address is --> \n{error}\n")

print("------------------------------------------- current_dir info -----------------------------------------------")

cmd_2 = "dir"

current_dir_info = subprocess.Popen(cmd_2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
current_dir_info.wait()

return_code_2 = current_dir_info.wait()
output_2, error_2 = current_dir_info.communicate()

print(f"Return code of current_dir_info is --> {return_code_2}\n")
print(f"Output of current_dir_info is --> \n{output_2}\n")
print(f"Error of current_dir_info is --> \n{error_2}")

print("------------------------------------------- python_version -----------------------------------------------")

cmd_3 = "python -V"

python_version = subprocess.Popen(cmd_3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
python_version.wait()

return_code_3 = python_version.wait()
output_3, error_3 = python_version.communicate()

print(f"Return code of python_version is --> {return_code_3}\n")
print(f"Output of python_version is --> \n{output_3}\n")
print(f"Error of python_version is --> \n{error_3}")

