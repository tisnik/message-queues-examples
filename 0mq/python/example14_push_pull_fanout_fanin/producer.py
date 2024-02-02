from time import sleep

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PUSH
PORT = 5556


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


@context()
@socket(CONNECTION_TYPE)
def start_producer(context, socket):
    """Spuštění serveru."""

    address = "tcp://*:{port}".format(port=PORT)
    # socket.set_hwm(1)
    socket.bind(address)
    print("Bound to address {a}".format(a=address))

    for i in range(101):
        send_message(socket, "Message #{i}".format(i=i))
        sleep(0.1)


start_producer()
