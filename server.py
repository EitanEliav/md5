import multiprocessing
import socket
import threading
class ser:
    def __init__(self,host,port, constlen:int):
        self.host = host
        self.port = port
        self.clients = []
        self.len = constlen
        self.constlen = constlen
        self.max_client = multiprocessing.cpu_count()
        self.start_num = "0" * self.len
        self.numguessess = 10 ** self.len
        self.chunk = str(self.numguessess // self.max_client)
        self.lock = threading.Lock()

        self.server_socket = socket.socket()

    def initiate_connection(self):
        self.server_socket.bind(('0.0.0.0',8200))
        self.server_socket.listen()
    def start(self):
        while True:
            client_socket, client_addrs = self.server_socket.accept()
            newuser = user(client_socket)
            threading.Thread(target=newuser.handle_client, daemon=True).start()


class user:
    def __init__(self, socket):
        self.socket = socket

    def handle_client(self, client_socket : socket.socket ,addr):
        while True:
            data = self.socket.recv(1024)
            print(data)