import socket
from .loader import *

ld = Loader()

class Connection:

    def __init__(self):
        self.reference = "www.google.com"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def check_connection(self):
        ld.load("Checking connection...")
        try:
            self.sock.connect_ex((self.reference, 80))
            return True
        except Exception as e:
            print("\nConnection Error, try again")
            return False

            