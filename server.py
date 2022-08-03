"""Module for Sockets"""
import socket
    # Citation for the following function:
    # Date: 6/22/2022
    # Copied from /OR/ Adapted from /OR/ Based on:
    # Source URL:
    # https://docs.python.org/3/howto/sockets.html,
    # https://realpython.com/python-sockets/

class Server():
    """Server Class"""
    def __init__(self) -> None:
        pass

    def server(self):
        """function that starts server and listner"""
        # data to send back to connection

        # create socket object
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the loopback adress and the port to the socket
        serversocket.bind(('localhost', 8002))
        #open 5 connections to create sockets
        serversocket.listen(5)
        # accpet connections conn will be socket object and adder is
        # where the request is coming from
        # https://docs.python.org/3/library/socket.html#socket.socket.accept
        conn, addr = serversocket.accept()
        # Citation for the following function:
        # Date: 6/22/2022
        # Copied from /OR/ Adapted from /OR/ Based on:
        # Source URL:  https://realpython.com/python-sockets/
        # open connection object
        with conn:
            # print out the connecting adder to console
            print(f"Connected by {addr}")
            # loop until no data is recived
            while True:
                data = conn.recv(1024)
                # print data from connect with the browser
                print(data)
                # break loop when done
                if not data:
                    break
                # send the welcome message back to the socket
if __name__ == "__main__":
    Server.server(None)
