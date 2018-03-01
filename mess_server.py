# mess_server.py


import socket
import sys

def Main():
    shutdown = False  # Parameter that defines if the program closes

    try:
        # We open a TCP socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as msg:
        print('Failed to create socket. Socket Error code: %s'% msg + '. Exiting...')
        sys.exit()

    except TypeError as msg:
        print("Failed to create socket. Type Error: %s" % msg+ '. Exiting...')
        sys.exit()

    print('Socket initialized.')

    HOST = ''       # General host for all available interfaces
    port = 9876     # Generic un-privileged port

    try:
        # Bind the socket to the port
        serversocket.bind((HOST, port))

    except socket.error as msg:
        print('Failed to bind socket to %s:%s. Socket Error code: %s . Exiting...' % (str(HOST), str(port), msg))
        sys.exit()

    except TypeError as msg:
        print('Failed to bind socket to %s:%s. Type Error code: %s . Exiting...' % (str(HOST), str(port), msg))
        sys.exit()

    print('Socket bind to %s:%s.' % (str(HOST), str(port)))

    try:
        # Opening to listen
        serversocket.listen(5)

    except socket.error as msg:
        print('Failed to listen to %s:%s. Socket Error code: %s . Exiting...' % (str(HOST), str(port), msg))
        sys.exit()

    except TypeError as msg:
        print('Failed to listen to %s:%s. Type Error code: %s . Exiting...' % (str(HOST), str(port), msg))
        sys.exit()

    print('Socket listening to %s:%s.' % (str(HOST), str(port)))

    try:
        conn, addr = serversocket.accept()

    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        shutdown = True

    except socket.error as msg:
        print('Failed to connect to clients. Socket Error code: %s . Exiting...' % msg)
        sys.exit()

    except TypeError as msg:
        print('Failed to connect to clients . Type Error code: %s . Exiting...' % msg)
        sys.exit()


    while not shutdown:
        try:
            print('Connection from : %s' % str(addr))
            data = conn.recv(1024).decode()
            if not data:
                break
            print('From Connected User: ' + str(data))
            data = input(" > ")
            conn.senda(data.encode())
        except KeyboardInterrupt:
            shutdown = True
            print('Keyboard Interrupt. Shuting Down...')
            continue
    serversocket.close()
    print('Socket Closed.')


if __name__ == '__main__':
    Main()
