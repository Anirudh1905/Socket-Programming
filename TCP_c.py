import socket

s=socket.socket()
host=socket.gethostname()
port=9999
s.connect((host,port))

num=(input())	
s.send(num.encode())
s.close()
