import socket
from time import ctime
import threading

s=socket.socket()
host=socket.gethostname()
port=9999
s.connect((host,port))

def receive():
    while True:
        rMessage = s.recv(1024)
        if rMessage.decode()=='bye':
            print ("Ending connection")
            break
        print ("[{0}]: {1}".format(ctime(), rMessage.decode()))

def send():
    while True:
        sMessage = input(">>")
        s.send(sMessage.encode())

t1 = threading.Thread(target=send, name=1)
t2 = threading.Thread(target=receive, name=2)

t1.start()
t2.start()
