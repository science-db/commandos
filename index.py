#!/user/bin/env python3
import subprocess
import platform
import socket
import time
import os
import py_compile
import PyQt5.QtWidgets
import PyQt5.QtGui
import PyQt5.QtCore
import PyQt5.QtWebEngineWidgets
import testfactor


host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("command.os VEVO2")
print("-http/-ip/date/cls/-a dir")
while True:
	code = input("n? ")
	if code == '-http':
		host = input("Enter Website To Ping: ")
		number = input("Enter How Many Times To Ping: ")

		def ping(host):
			param = '-n' if platform.system().lower() == 'windows' else '-c'
			command = ['ping', param, number, host]
			return subprocess.call(command)
		print(ping(host))
	if code == '-ip':
		print("Your Local IPS Is: " + host_ip)
		print("Your Desktop Name Is: " + host_name)
	if code == 'date':
		print("The Local Date Is: " + time.strftime("%m/%d/%Y"))
	if code == 'cls':
		dir_list = os.listdir(path)
		print("Files and Directories in '", path, "' :")
		print(dir_list)
	if code == '-a dir':
		file = input("Enter The Direct File Path To Read: ")
		dir_list2 = os.listdir(file)
		print("Files and directories in '", file, "':")
		print(dir_list2)