import subprocess

subprocess_obj = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  universal_newlines=True)

return_code = subprocess_obj.wait()

out, err = subprocess_obj.communicate()

print(f"The Return code : {return_code}")
print(f"The output : \n{out}")
print(f"The error : \n{err}")
