import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.SUB
PORT1 = 5556
PORT2 = 5557


def connect(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))


@context()
@socket(CONNECTION_TYPE)
def start_subscriber(ports, context, socket):
    """Spuštění příjemce."""
    for port in ports:
        connect(socket, port)
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    print("Waiting for messages...")

    while True:
        message = socket.recv_string()
        print("Received message '{m}'".format(m=message))


start_subscriber((PORT1, PORT2))
