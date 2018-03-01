# multy_ser.py
# Done without erro handling, becouse it is messy to read


import socket
import threading
import sys


class clientconnection():
    """This class handles the connections from different clients, accepts the connection with the client"""
    def __init__(self, serversocket):
        self.serversocket = serversocket
        self.conn = 0
        self.addr = 0
        global shutdown
        self.conn, self.addr = self.serversocket.accept()
        print('Connection established with %s' % str(self.addr))


def s2c(client):
    """Handles outgoing messages"""
    conn = client.conn
    while not shutdown:
        data = input(" > ")
        conn.send(data.encode())


def c2s(client):
    """Handles incoming messages"""
    global shutdown
    conn = client.conn
    while not shutdown:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('From Connected User: ' + str(data))

def main():
    global shutdown
    # We open a TCP socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket initialized.')

    HOST = ''       # General host for all available interfaces
    port = 9876     # Generic un-privileged port

    # Bind the socket to the port
    serversocket.bind((HOST, port))

    print('Socket bind to %s:%s.' % (str(HOST), str(port)))

    # Opening to listen
    serversocket.listen(5)
    print('Socket listening to %s:%s.' % (str(HOST), str(port)))

    # Aquiring the client connection
    client = clientconnection(serversocket)

    # Starting the conversation
    threading.Thread(s2c(client))
    threading.Thread(c2s(client))
    serversocket.close()
    print('Exiting')
    return 0


if __name__ == '__main__':
    shutdown = False
    main()
