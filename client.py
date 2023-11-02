import hashlib
import socket

class client:
    def __init__(self):
        self.socket = socket.socket()

    def main_client(self):
        self.socket.connect(('127.0.0.1',8200))

secret = '12345'
length = len(secret)
p = hashlib.md5(secret.encode()).hexdigest()


def encrypt_guess(guess):

    my_guess = hashlib.md5(guess.encode()).hexdigest()
    return my_guess


def find_secret(start, end):
    for i in range(start, end):
        guess = str(i).zfill(length)
        if encrypt_guess(guess) == p:
            print(guess)
            return True, guess
    return False, None


if __name__ == "__main__":
    for i in range(0, 10**length, 100):
        print(f"range = [{i}, {i+100}]")
        status, res = find_secret(i, i+100)
        if status:
            print(f"found --> {res}")
            break
