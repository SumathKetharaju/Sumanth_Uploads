import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect("10.239.247.213", 22,  "username", "password")
stdin, stdout, stderr = client.exec_command("ls -l")
#ssdrive is username
# ls-l : to list directories and this for linux

# 22 port here
