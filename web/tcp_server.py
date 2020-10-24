import socket
import datetime

HOST='0.0.0.0'
PORT= 3434

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

s.listen(1)

while True:
    conn,addr = s.accept()
    print("Client %s connected!" %str(addr))
    dt = datetime.datetime.now()
    message = "Current time is " + str(dt)
    conn.send(message.encode('utf8'))
    print("Sent: ",message)
    conn.close

