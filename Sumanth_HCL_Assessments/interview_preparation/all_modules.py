import paramiko
import nmap
import subprocess
import winrm
import openpyxl
import json
import csv
import os
import logging
import re
import requests
import sys

# print("--------------------------------------------- Paramiko ------------------------------------------------------")
#
# ssh = paramiko.SSHClient()
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh.connect(hostname="", username="", password="", port=22)
#
# local_path = ""
#
# destination_path = ""
#
# sftp_client = ssh.open_sftp()
#
# sftp_client.get(local_path, destination_path)
# sftp_client.put(destination_path, local_path)
#
# sftp_client.close()
#
# ssh.close()
#
#
# print("--------------------------------------------- nmap ------------------------------------------------------")
#
# ip_address = input("Please Enter Valid Ip address --> ")
#
# min_port_number = int(input("Please Enter Minimum Port number --> "))
#
# max_port_number = int(input("Please Enter Maximum Port number --> "))
#
# port_scanner = nmap.PortScanner()
#
# for port_number in range(min_port_number, max_port_number):
#     scan_ip_port = port_scanner.scan(ip_address, str(port_number))
#     port_status = scan_ip_port["scan"][ip_address]["tcp"][port_scanner]["status"]
#     print(f"Port Status is --> {port_status}")

# print("--------------------------------------------- subprocess Popen ------------------------------------------------------")
# print("--------------------------------------------- host name ------------------------------------------------------")
#
# cmd = "ipconfig"
#
# # if you run this the output would be in binary
# # know_hostname = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
# # if you run this program the output would be in binary,so we need to use universal_newlines=True
# # to get the output as string
# # know_hostname = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
#
# know_hostname = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#
# know_hostname.wait()
#
# return_code = know_hostname.wait()
#
# output, error = know_hostname.communicate()
#
# print(f"Return code of host name is --> {return_code}\n")
# print(f"Output of host nameis --> \n{output}\n")
# print(f"Error of host nameis --> \n{error}\n")
#
# print("------------------------------------------- current_dir info -----------------------------------------------")
#
# cmd_2 = "dir"
#
# current_dir_info = subprocess.Popen(cmd_2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#
# current_dir_info.wait()
#
# return_code_2 = current_dir_info.wait()
#
# output_2, error_2 = current_dir_info.communicate()
#
# print(f"Return code of current_dir_info is --> {return_code_2}\n")
# print(f"Output of current_dir_info is --> \n{output_2}\n")
# print(f"Error of current_dir_info is --> \n{error_2}")
#
# print("------------------------------------------- python_version -----------------------------------------------")
# cmd_3 = "python -V"
#
# python_version = subprocess.Popen(cmd_3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#
# python_version.wait()
#
# return_code_2 = python_version.wait()
#
# output_2, error_2 = python_version.communicate()
#
# print(f"Return code of python_version is --> {return_code_2}\n")
# print(f"Output of python_version is --> \n{output_2}\n")
# print(f"Error of python_version is --> \n{error_2}")

# print("--------------------------------------------- subprocess run ------------------------------------------------------")

