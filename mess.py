# mess_server.py


import socket
import sys


def Main():
    shutdown = False  # Parameter that defines if the program closes

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

    # Accepting clients
    conn, addr = serversocket.accept()
    print('Connection from : %s' % str(addr))

    while not shutdown:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('From Connected User: ' + str(data))
        data = input(" > ")
        conn.send(data.encode())
    serversocket.close()
    print('Socket Closed.')


if __name__ == '__main__':
    Main()
