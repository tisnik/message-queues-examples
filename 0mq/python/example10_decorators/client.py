import zmq
from zmq.decorators import context, socket


CONNECTION_TYPE = zmq.PAIR
PORT = 5556


@context()
@socket(CONNECTION_TYPE)
def start_client(context, socket):
    """Spuštění klienta."""

    address = "tcp://localhost:{port}".format(port=PORT)
    socket.connect(address)
    print("Connected to {a}".format(a=address))

    print("Waiting for message...")
    while True:
        message = socket.recv_string()
        print("Received message '{m}'".format(m=message))


start_client()
