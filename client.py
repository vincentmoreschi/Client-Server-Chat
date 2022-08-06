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
    def sendmessage(self,message):
        """Send message over connection"""
        self.sock.sendall(message)
    def recvmessage(self):
        """Get message
        """
        # Citation for the following function:
        # Date: 6/22/2022
        # Adapted from
        # Source URL:  https://realpython.com/python-sockets/,https://docs.python.org/3/howto/sockets.html
        # get reciving data
        chunks = []
        bytes_recd = 0
        chunk = self.sock.recv(1024)
        # get length of incoming message
        msglen = int(chunk.decode()[0])
        # delete size
        chunk = chunk[1:]
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
        while bytes_recd < msglen:
            chunk = self.sock.recv(min(msglen - bytes_recd, 1024))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
        
if __name__ == "__main__":
    msg = ''
    client = Client()
    print("Connecting to server....")
    client.connect()
    print("Connection successful, Welcome to the chat room!")
    print("Enter a message")
    while True:
        # ask for input
        msg = input(">")
        # add string size to first part of message so the server
        # knows how many bytes to expect and send message
        client.sendmessage(str.encode(f'{len(msg)}{msg}'))
        #get response from server
        print(client.recvmessage().decode())
