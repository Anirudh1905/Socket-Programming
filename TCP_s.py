import socket

s=socket.socket()
host=socket.gethostname()
port=9999	
s.bind((host,port))
s.listen(5)
print("Waiting for clients...")
conn,addr = s.accept()	        
print("Connected by ", addr)
data=conn.recv(1024)
print(data.decode())
conn.close()
