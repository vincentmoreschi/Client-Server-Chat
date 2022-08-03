"""Module for Sockets"""
import socket

class Client:
    """Client class to connect to Server"""
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    def connect(self):
        """Create Connection"""
        self.sock.connect(('localhost', 8002))
    def sendmessage(self,msg):

        sent = self.sock.send(msg)


if __name__ == "__main__":
    connection = Client()
    connection.connect()
    connection.sendmessage(b"test")