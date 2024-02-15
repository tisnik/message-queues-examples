from sys import argv, exit

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.SUB
PORT = 5557


def connect(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))


@context()
@socket(CONNECTION_TYPE)
def start_subscriber(filter, port, context, socket):
    """Spuštění příjemce."""
    connect(socket, port)
    socket.setsockopt_string(zmq.SUBSCRIBE, filter)

    print("Waiting for messages...")

    while True:
        message = socket.recv_string()
        print("Received message '{m}'".format(m=message))


if len(argv) <= 1:
    print("Please provide filter on the CLI")
    exit(1)


start_subscriber(argv[1], PORT)
