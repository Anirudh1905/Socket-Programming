import socket

c=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host=socket.gethostname()
port=9999

while True:
    num=(input())
    if 'Bye' in num:
        c.sendto(num.encode(),(host,port))
        break
    c.sendto(num.encode(),(host,port))
    print(c.recvfrom(1024)[0].decode())
    f=open('a.txt','r')
    print(f.read())
c.close()
