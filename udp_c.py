import socket

c=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host=socket.gethostname()
port=9999

while True:
    num=(input())
    c.sendto(num.encode(),(host,port))
    data,addr=c.recvfrom(1024)
    if 'Bye' in data.decode():
        c.sendto('Bye'.encode(),(host,port))
        break
    print("Server: ",data.decode())

c.close()
