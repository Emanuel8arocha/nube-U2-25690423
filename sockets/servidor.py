import socket
s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen()
con, dir = s.accept()
while True:
    dato = con.recv(1024)
    print(dato.decode)
    if not dato:
        break
    con.send(b"eco: " + dato)
    