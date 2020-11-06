import socket

s=socket.socket()
host=socket.gethostname()
port=9999
s.connect((host,port))
print("Give input")

num=int(input())
if num==1:
    s.send('date'.encode())
    print(s.recv(1024).decode())
else:
    s.send('BYe'.encode())

s.close()
