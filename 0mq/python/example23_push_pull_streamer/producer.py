import zmq
from zmq.decorators import context, socket
import time


CONNECTION_TYPE = zmq.PUSH
PORT = 5550


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


@context()
@socket(CONNECTION_TYPE)
def start_producer(port, context, socket):
    """Spuštění serveru."""

    address = "tcp://localhost:{port}".format(port=port)
    # socket.set_hwm(1)
    socket.connect(address)
    print("Connected to address {a}".format(a=address))

    for i in range(100):
        send_message(socket, "Message #{i}".format(i=i))
        time.sleep(0.2)


start_producer(PORT)
