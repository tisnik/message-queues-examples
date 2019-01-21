import zmq
from zmq.decorators import context, socket
import time


CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


@context()
@socket(CONNECTION_TYPE)
def start_server(context, socket):
    """Spuštění serveru."""

    address = "tcp://*:{port}".format(port=PORT)
    socket.bind(address)
    print("Bound to address {a}".format(a=address))

    for i in range(10):
        send_message(socket, "Message #{i}".format(i=i))
        time.sleep(1)


start_server()
