import socket

c=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host=socket.gethostname()
port=9999

while True:
    num=(input())
    c.sendto(num.encode(),(host,port))
    if 'Bye' in num:
        break
    print(c.recvfrom(1024)[0].decode())
    f=open('b.txt','r')
    print(f.read())

c.close()
