# vim: set fileencoding=utf-8

from time import sleep
from nanomsg import Socket, SUB, SUB_SUBSCRIBE

URL = "ipc:///tmp/example10"


def receive_message(socket):
    message = socket.recv()
    print("Received message: '{}'".format(message))


with Socket(SUB) as socket:
    print("Socket created")

    socket.connect(URL)
    socket.set_string_option(SUB, SUB_SUBSCRIBE, "Message B")
    print("Connected to URL {}".format(URL))

    while True:
        receive_message(socket)

print("Socket closed")
