import socket
import threading
class ser:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.clients = []
        self.socket = socket.socket()

    def initiate_connection(self):
        self.socket.bind(('0.0.0.0',8200))
        self.socket.listen()
    def start(self):
        while True:
            client_socket, client_addrs = self.socket.accept()
            newuser = user(client_socket)
            threading.Thread(target=newuser.handle_client, daemon=True).start()


class user:
    def __init__(self, socket):
        self.socket = socket

    def handle_client(self):
        while True:
            data = self.socket.recv(1024)
            print(data)