import zmq

CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def start_client():
    """Spuštění klienta."""

    with zmq.Context() as context:
        with context.socket(CONNECTION_TYPE) as socket:
            address = "tcp://localhost:{port}".format(port=PORT)
            socket.connect(address)
            print("Connected to {a}".format(a=address))

            print("Waiting for message...")
            while True:
                message = socket.recv_string()
                print("Received message '{m}'".format(m=message))


start_client()
