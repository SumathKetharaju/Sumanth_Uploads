import subprocess

standard_input = subprocess.Popen(stdin="ipconfig", stdout="", stderr="")

print(standard_input)