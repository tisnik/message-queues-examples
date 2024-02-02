from os import getpid
from time import sleep

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PUB
PORT = 5556


def bind(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://*:{port}".format(port=port)
    socket.bind(address)
    print("Bound to {a}".format(a=address))


def publish_message(socket, message):
    """Publikování zprávy zprávy."""
    print("Publishing message '{m}'".format(m=message))
    socket.send_string(message)


@context()
@socket(CONNECTION_TYPE)
def start_publisher(port, context, socket):
    """Spuštění publisheru."""
    pid = getpid()
    print("Publisher PID={pid}".format(pid=pid))

    bind(socket, port)
    for i in range(100):
        message = "Message #{i} from {pid}".format(i=i, pid=pid)
        publish_message(socket, message)
        sleep(1)


start_publisher(PORT)
