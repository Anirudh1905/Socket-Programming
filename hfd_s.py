import socket

s=socket.socket()
host=socket.gethostname()
port=9999	
s.bind((host,port))
s.listen(5)
print("Waiting for clients...")
conn,addr = s.accept()	        
print("Connected by ", addr)

while True:
    data=conn.recv(1024)
    if 'Bye' in data.decode():
        conn.send('Bye'.encode())
        break
    print("Client: ",data.decode())
    x=input()
    conn.send(x.encode())

conn.close()
