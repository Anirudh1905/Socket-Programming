import socket
import os 
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
    os.system('arp -a '+data.decode()+'>aa.txt')
    print("Client: ",data.decode())
    conn.send("Command executed".encode())

conn.close()
