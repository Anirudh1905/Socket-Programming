import socket
from time import ctime
from datetime import date
import threading

s=socket.socket()
host=socket.gethostname()
port=9999
s.bind((host,port))
s.listen(5)
print("Waiting for clients...")
conn,addr = s.accept()
print("Connected by ", addr)


def receive():
    while True:
        rMessage = conn.recv(1024)
        if rMessage.decode()=='Bye':
            print ("Ending connection")
            conn.send('Bye'.encode())
            break
        print(ctime(),rMessage.decode())
        print ("[{0}]: {1}".format(ctime(), rMessage.decode()))


def send():
    while True:
        sMessage = input(">>")
        if not sMessage:
            break
        conn.send(sMessage.encode())

t1 = threading.Thread(target=send, name=3)
t2 = threading.Thread(target=receive, name=4)

t1.start()
t2.start()

