import paramiko
import openpyxl
import json
import re
import subprocess
import nmap
import winrm
import pylint
import csv
import logging

ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname="", username="", password="", port=22)

local_path = ""

destination_path = ""

sftp_client = ssh_client.open_sftp()

sftp_client.get(local_path, destination_path)
sftp_client.put(local_path, destination_path)

sftp_client.close()

ssh_client.close()
