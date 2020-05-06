import socket
import random
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "127.0.0.1"
port = 5555
addr = (server, port)

client.connect(addr)

a = [x for x in range(5)]

while True:
    x = input()
    client.send(pickle.dumps(x))
    print("Got:", pickle.loads(client.recv(2048)))
