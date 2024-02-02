import time

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PULL
PORT = 5556


@context()
@socket(CONNECTION_TYPE)
def start_consumer(context, socket):
    """Spuštění konzumenta."""

    address = "tcp://localhost:{port}".format(port=PORT)
    socket.connect(address)
    print("Connected to {a}".format(a=address))

    print("Waiting for message...")
    cnt = 0
    while True:
        message = socket.recv_string()
        cnt += 1
        print("Received message {c} of 100: '{m}'".format(c=cnt, m=message))
        time.sleep(0)


start_consumer()
