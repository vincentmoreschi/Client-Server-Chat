"""Module for Sockets"""
from email import message
import socket

# Citation for the following function:
# Date: 6/22/2022
# Copied from /OR/ Adapted from /OR/ Based on:
# Source URL:
# https://docs.python.org/3/howto/sockets.html,
# https://realpython.com/python-sockets/


class Server:
    """Server Class"""

    def __init__(self) -> None:
        pass

    def server(self):
        """function that starts server and list"""
        # data to send back to connection

        # create socket object
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the loopback adress and the port to the socket
        serversocket.bind(("localhost", 8002))
        # open 5 connections to create sockets
        serversocket.listen(5)
        # accpet connections conn will be socket object and adder is
        # where the request is coming from
        # https://docs.python.org/3/library/socket.html#socket.socket.accept
        conn, addr = serversocket.accept()
        # Citation for the following function:
        # Date: 6/22/2022
        # Copied from /OR/ Adapted from /OR/ Based on:
        # Source URL:  https://realpython.com/python-sockets/,https://docs.python.org/3/howto/sockets.html
        # open connection object
        with conn:
            response = b""
            # print out the connecting adder to console
            print(f"Connected by {addr}")
            print("Waiting for message")
            # loop until no data is recived
            while True:
                packet = conn.recv(1024)
                if not packet:
                    break
                # add to the response
                response = response + packet
                if(response.decode() == "/q"):
                    conn.close()
                    break
                if(response):
                    response = response[1:]
                    print(response.decode())
                    msg = input(">")
                    conn.send(str.encode(f'{len(msg)}{msg}'))
                    response =b''
                
            
                
                


if __name__ == "__main__":
    Server.server(None)
