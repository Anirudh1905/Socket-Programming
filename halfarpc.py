import socket

s=socket.socket()
host=socket.gethostname()
port=9999
s.connect((host,port))

while True:
    num=(input())
    if 'Bye' in num:
        break
    s.send(num.encode())
    print(s.recv(1024).decode())
    f=open('aa.txt','r')
    print(f.read())
s.close()
