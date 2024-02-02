import time

import zmq
from message import Message
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def send_serialized_object(socket, obj, i):
    """Poslání zprávy."""
    print("Sending message #{i}'".format(i=i))
    socket.send_pyobj(obj)


@context()
@socket(CONNECTION_TYPE)
def start_server(context, socket):
    """Spuštění serveru."""

    address = "tcp://*:{port}".format(port=PORT)
    socket.bind(address)
    print("Bound to address {a}".format(a=address))

    for i in range(10):
        m = Message(i)
        send_serialized_object(socket, m, i)
        time.sleep(1)


start_server()
