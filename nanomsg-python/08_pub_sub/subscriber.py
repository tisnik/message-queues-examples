from time import sleep
from nanomsg import Socket, SUB, SUB_SUBSCRIBE

URL = "ipc:///tmp/example8"


def receive_message(socket):
    message = socket.recv()
    print("Received message: '{}'".format(message))


with Socket(SUB) as socket:
    print("Socket created")

    socket.connect(URL)
    print("Connected to URL {}".format(URL))

    while True:
        receive_message(socket)

print("Socket closed")
