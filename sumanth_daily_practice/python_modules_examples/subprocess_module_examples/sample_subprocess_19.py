import subprocess
# cmd_1 = r"C:\Users\SUMANTH\Desktop\sumanth_daily_practice"
cmd = "python"
# subprocess_obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
subprocess_obj_2 = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# return_code = subprocess_obj.wait()
# out, err = subprocess_obj.communicate()
# print("output", subprocess_obj.stdout)
print("output", subprocess_obj_2.stdout)
# print("error", subprocess_obj.stderr)
print("error", subprocess_obj_2.stderr)
print("error", subprocess_obj_2.returncode)
