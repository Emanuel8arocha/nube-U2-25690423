import socket
s = socket.socket()
s.bind(("0.0.0.0", 5000))
s.listen()
con, dir = s.accept()
dato = con.recv(1024)
con.send(b"eco: "+ dato)