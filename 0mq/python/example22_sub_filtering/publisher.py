from sys import argv, exit
from time import sleep

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PUB
PORT = 5556


def connect(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))


def publish_message(socket, message):
    """Publikování zprávy zprávy."""
    print("Publishing message '{m}'".format(m=message))
    socket.send_string(message)


@context()
@socket(CONNECTION_TYPE)
def start_publisher(name, delay, port, context, socket):
    """Spuštění publisheru."""
    print("Publisher '{name}'".format(name=name))

    connect(socket, port)
    for i in range(100):
        message = "{name}: Message #{i}".format(name=name, i=i)
        publish_message(socket, message)
        sleep(delay)


if len(argv) <= 2:
    print('Please provide publisher name and sleep amount on the CLI')
    exit(1)


name = argv[1]
delay = float(argv[2])
start_publisher(name, delay, PORT)
