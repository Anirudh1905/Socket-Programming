import socket
import os

port = 6000
s = socket.socket()
host = '127.0.0.1'
s.bind((host, port))
s.listen(5)

conn, addr = s.accept()
filename = 'b.txt'

f = open(filename, 'r')
l = f.read()
conn.send(l.encode())

print('Done sending')
conn.close()
