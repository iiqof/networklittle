#mess_client

import socket
import sys

def Main():

    #shutdown = False  # Parameter that defines if the program closes

    try:
        # We open a TCP socket
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as msg:
        print('Failed to create socket. Socket Error code: %s'% msg + '. Exiting...')
        sys.exit()

    except TypeError as msg:
        print("Failed to create socket. Type Error: %s" % msg+ '. Exiting...')
        sys.exit()

    print('Socket initialized.')


    try:
        HOST = input('Server ip > ')
        port = input('Conection port >')
        # We connecto to the server
        clientsocket.connect((HOST, port))

    except socket.error as msg:
        print('Failed to connect to server. Socket Error code: %s'% msg + '. Exiting...')
        sys.exit()

    except TypeError as msg:
        print("Failed to connect to server. Type Error: %s" % msg+ '. Exiting...')
        sys.exit()

    print('Connection established.')
    mess = input('Say hello! > ')
    while mess != 'quit()':
        try:
            clientsocket.send(mess.encode())
            data = clientsocket.recv(1024).decode()
            print('Received from server: ' + str(data))
            mess = input(" > ")

        except KeyboardInterrupt:
            mess = 'quit()'
            print('Keyboard Interrupt.')
            continue

        except socket.error as msg:
            print('Failed to receive message from server. Socket Error code: %s' % msg + '. Exiting...')
            sys.exit()

        except TypeError as msg:
            print("Failed to receive message from server. Type Error: %s" % msg+ '. Exiting...')
            sys.exit()

    clientsocket.close()
    print('Socket closed...')
    print('Shutting down.')

if __name__ == '__main__':
    Main()