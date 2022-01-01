import paramiko

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname="192.168.55.105", username="SUMANTH", password="sumanth", port=22)


local_path = "product-info.json"

transferred_path = "C:\\Users\\SUMANTH\\Desktop\\K_S_DO"

sftp_client = ssh_client.open_sftp()

sftp_client.put("local_path", "transferred_path")
sftp_client.close()
ssh_client.close()


# This program is used to transfer a file from local server to remote server or viceversa
import paramiko

# paramiko module works by creating sshclient
ssh = paramiko.SSHClient()

# This is for asking yes or no confirmation while connecting remote server at very first time (or)
# simply it is add to your known host to on your local server
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# here we are connecting to remote server
ssh.connect(hostname="192.261.345", username="sumanth", password="sunil", port=22)

local_path = r"\home\ec2-user\paramiko.txt"

destination_path = "C:\\user\\downloads\\paramiko.txt"

# we need to transfer a file or download a file from remote server for that purpose we are creating sftp_client object
# from ssh_client, With this sftp_client we are opening sftp_client connection with your remote server
sftp_client = ssh.open_sftp()

# get - downloading file from remote server to our local server
sftp_client.get(local_path, destination_path)

# put - Transfer file from local server to remote server
sftp_client.put(local_path, destination_path)

sftp_client.close()
ssh.close()
