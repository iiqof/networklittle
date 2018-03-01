# echo_client.py
import socket

host = socket.gethostname()    
port = 44659                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
mess = raw_input('message>')
s.sendall(mess)
data = s.recv(1024)
s.close()
print('Received', repr(data))
