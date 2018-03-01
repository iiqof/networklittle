import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 44659
serversocket.bind((host, port)) 
serversocket.listen(1)

conn, addr = serversocket.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
