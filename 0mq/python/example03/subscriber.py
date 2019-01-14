import zmq


def connect(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))
    return socket


def start_subscriber():
    """Spuštění příjemce."""
    socket = connect(5556, zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    print("Waiting for messages...")
    while True:
        message = socket.recv_string()
        print("Received message '{m}'".format(m=message))


start_subscriber()
