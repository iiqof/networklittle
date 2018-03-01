# Server, recieves conections form clients

import socket

class Server():
    """Funcitonality of the server in this"""
    def __init__(self, host='', port=9876, backlog=5):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.s = 0 # Will hold the socket instance


    def deploy(self):
        """Opens the server and binds the socket to the port, starts listening"""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
        self.s.bind((self.host, self.port))
        self.s.listen(self.backlog)
        return 1

    def printaddress(self):
        print('Server adress \'%s\':%s' % (str(self.host), str(self.port)))
        return 1

    def shutdownserver(self):
        if self.s != 0:
            self.s.close()
            print('Socket Closed...')
        print('Shutting down...')


if __name__ == '__main__':
    server = Server(port=6009)
    server.deploy()
    server.printaddress()
    server.shutdownserver()
    print(' ')
