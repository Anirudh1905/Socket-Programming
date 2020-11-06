import socket
import time

s=socket.socket()
host=socket.gethostname()
port=9999	
s.bind((host,port))
s.listen(5)
print("Waiting for clients...")
conn,addr = s.accept()	        
print("Connected by ", conn)
data=conn.recv(1024)
print(data.decode())

if 'date' in data.decode():
    t=time.asctime(time.localtime(time.time()))
    conn.sendall(t.encode())

conn.close()
