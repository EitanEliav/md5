import hashlib
import socket
from threading import Thread
import multiprocessing

class Secret:
    secret = '12345'
#hello
class client:
    WORK = 1
    FINISH = 2
    def __init__(self, secret):
        self.socket = socket.socket()
        self.secret = secret
        self.start = -1
        self.end = -1
        self.result = None
        self.status = client.WORK
    def main_client(self):
        self.socket.connect(('127.0.0.1',8200))

    def set_work(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def encrypt_guess(guess):

        my_guess = hashlib.md5(guess.encode()).hexdigest()
        return my_guess

    def find_secret(self):
        for i in range(self.start, self.end):
            if self.status == client.FINISH:
                return

            guess = str(i).zfill(len(Secret.secret))
            if client.encrypt_guess(guess) == self.secret:

                self.result = guess


def main():
    length = len(Secret.secret)
    p = client.encrypt_guess(Secret.secret)

    cpu_count = multiprocessing.cpu_count()
    clients = []
    threads = []
    chunk = 10**length/cpu_count
    for i in range(cpu_count):
        start = int(i * chunk)
        end = int((i + 1) * chunk)
        my_client = client(p)
        my_client.set_work(start, end)
        clients.append(my_client)
        my_thread = Thread(target=my_client.find_secret)
        threads.append(my_thread)
        my_thread.start()

    found = False
    while not found:
        for i in range(cpu_count):
            if not threads[i].is_alive():
                if clients[i].result == None:
                    pass
                else:
                    print(f"found -> {clients[i].result}")
                    found = True
                    for j in range(cpu_count):
                        clients[j].status = client.FINISH
                    break





if __name__ == "__main__":
    main()
