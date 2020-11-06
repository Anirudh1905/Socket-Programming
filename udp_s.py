import socket

s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host=socket.gethostname()
port=9999	
s.bind((host,port))

print("UDP server up and listening")

while True:
    data,addr=s.recvfrom(1024)
    if 'Bye' in data.decode():
        s.sendto('Bye'.encode(),addr)
        break
    print("Client: ",data.decode())
    x=input()
    s.sendto(x.encode(),addr)
s.close()

