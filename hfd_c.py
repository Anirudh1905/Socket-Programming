import socket

s=socket.socket()
host=socket.gethostname()
port=9999
s.connect((host,port))

while True:
    num=(input())
    s.send(num.encode())
    t=s.recv(1024)
    if 'Bye' in t.decode():
        break
    print("Server: ",t.decode())

s.close()
