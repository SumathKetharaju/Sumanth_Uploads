# This program is used to transfer a file from local server to remote server or viceversa
import paramiko

# paramiko module works by creating sshclient
ssh_client = paramiko.SSHClient()

# This is for asking yes or no confirmation while connecting remote server at very first time (or)
# simply it is add to your known host on your local server
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# here we are connecting to remote server
ssh_client.connect(hostname="", username="", password="", port=22)

local_path = ""

destination_path = ""

# we need to transfer a file or download a file from remote server for that purpose we are creating sftp_client object
# from ssh_client, With this sftp_client we are opening sftp_client connection with your remote server
sftp_client = ssh_client.open_sftp()

# get - downloading file from remote server to our local server,
# In this case local path is remote server and destination path is our local server
sftp_client.get(local_path, destination_path)

# put - Transfer file from local server to remote server
# In this case local path is our local server and destination path is remote server
sftp_client.put(local_path, destination_path)

sftp_client.close()

ssh_client.close()
