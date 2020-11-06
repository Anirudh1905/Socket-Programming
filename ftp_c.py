import socket

c = socket.socket()
host = '127.0.0.1'
port = 6000
c.connect((host, port))

file=open('ftp_file.txt','wb')
data=c.recv(1024)
file.write(data)

file.close()
print('Successfully received the file')
c.close()
print('connection closed')
