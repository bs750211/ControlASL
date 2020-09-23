import socket
import time
c = "50"
d = "51"
e = "52"
Server_ip = '192.168.20.192'
Port = 4003

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server = server.connect((Server_ip, Port))

dstrng = ""
while True:
    data_server = server.recv(1024).decode('utf-8')
    dstrng += data_server
    try:
        dstrng = dstrng.rstrip()
        dstrng = dstrng.strip()
        print(dstrng)
    except:
        print("This string does not comply with the UTF-8 standard")

while True:
    time.sleep(60)
    timeis = time.localtime()
    a = time.strftime('%M', timeis)
    if a == c:
        print("Alert Time "+ a)
    if a == d:
        print("Alert Time "+ d)
    if a == e:
        print("Alert Time "+ e)