import socket
c = socket.socket()
c.connect(("localhost",  5000))
c.send(b"hola")
print(c.recv(1024))


