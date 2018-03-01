#mess_client

import socket
import sys

def Main():

    # We open a TCP socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket initialized.')


    HOST = input('Server ip > ')
    if HOST == '':
        HOST = 'FireLink'
        print('default : ' +str(HOST) )
    port = input('Conection port >')
    if port == '':
        port = 9876
    print('default : ' + str(port))
    port = int(port)
    # We connecto to the server
    clientsocket.connect((HOST, port))

    print('Connection established.')
    mess = input('Say hello! > ')
    while mess != 'quit()':
        clientsocket.send(mess.encode())
        data = clientsocket.recv(1024).decode()
        print('Received from server: ' + str(data))
        mess = input(" > ")

    clientsocket.close()
    print('Socket closed...')
    print('Shutting down.')


if __name__ == '__main__':
    Main()