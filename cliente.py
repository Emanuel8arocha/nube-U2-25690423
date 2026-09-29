import socket
c = socket.socket()
c.connect(("localhost", 5000))
while True:
    dato = input("mensaje : ")
    c.send(dato.ecode())
    if dato == "salir":
        break
    print(c.recv(1024).decode())

