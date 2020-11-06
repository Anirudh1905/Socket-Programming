import socket
import os

s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host=socket.gethostname()
port=9999	
s.bind((host,port))

print("UDP server up and listening")

while True:
    data,addr=s.recvfrom(1024)
    if 'Bye' in data.decode():
        break
    print("Client: ",data.decode())
    os.system("arp -a "+data.decode()+'>b.txt')
    s.sendto("command executed".encode(),addr)
s.close()

