import zmq
from zmq.decorators import context


CONNECTION_TYPE = zmq.PAIR
PORT = 5556


@context()
def start_client(context):
    """Spuštění klienta."""

    with context.socket(CONNECTION_TYPE) as socket:
        address = "tcp://localhost:{port}".format(port=PORT)
        socket.connect(address)
        print("Connected to {a}".format(a=address))

        print("Waiting for message...")
        while True:
            message = socket.recv_string()
            print("Received message '{m}'".format(m=message))


start_client()
