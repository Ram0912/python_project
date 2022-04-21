import time
import socket
import sys
import os
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind(('', port))
s.listen()
conn, addr = s.accept()
print(addr, "is connected to server")
command = input(str("enter command : "))
conn.send(command.encode())
print("command has been sent successfully")
data = conn.recv(1024)
if data:
    print("command recieved and executed successfully")
