from time import sleep

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PULL
PORT = 5557


@context()
@socket(CONNECTION_TYPE)
def start_collector(context, socket):
    """Spuštění sběratele."""

    address = "tcp://*:{port}".format(port=PORT)
    socket.bind(address)
    print("Connected to {a}".format(a=address))

    print("Waiting for message...")
    while True:
        message = socket.recv_string()
        print("Collecting message: '{m}'".format(m=message))
        sleep(0)


start_collector()
