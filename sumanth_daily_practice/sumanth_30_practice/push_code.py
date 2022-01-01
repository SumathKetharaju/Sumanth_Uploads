import subprocess

PRESENT_DIR = r"cd C:\Users\SUMANTH\Desktop\raviteja_github_demonstration\github_demonstration\github_demonstration"
STATUS_CMD = r"git status"
ADD_CMD = r"git add ."
COMMIT_CMD = r"git commit -m 30-Nov-2021"
PUSH_CMD = r"git push -u origin main"

print("--------------------------Entering Required directory------------------------------------")
subprocess_obj = subprocess.run(PRESENT_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
print(f"output:\n{subprocess_obj.stdout}\nerror:\n{subprocess_obj.stderr}\nrc:\n{subprocess_obj.returncode}")

print("--------------------------------Status files to git----------------------------")
subprocess_obj = subprocess.run(STATUS_CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                universal_newlines=True)
print(f"output:\n{subprocess_obj.stdout}\nerror:\n{subprocess_obj.stderr}\nrc:\n{subprocess_obj.returncode}")
#
# print("---------------------------------Committing files to git--------------------------")
# subprocess_obj = subprocess.run(COMMIT_CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                                 universal_newlines=True)
# print(f"output:\n{subprocess_obj.stdout}\nerror:\n{subprocess_obj.stderr}\nrc:\n{subprocess_obj.returncode}")
#
# print("---------------------------------Pushing files to git-------------------------------")
# subprocess_obj = subprocess.run(PUSH_CMD, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
#                                 universal_newlines=True)
# print(f"output:\n{subprocess_obj.stdout}\nerror:\n{subprocess_obj.stderr}\nrc:\n{subprocess_obj.returncode}")


