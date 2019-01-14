import zmq


def connect(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))
    return context, socket


def start_client():
    """Spuštění klienta."""
    try:
        context, socket = connect(5556, zmq.PAIR)
        print("Waiting for messages...")
        while True:
            message = socket.recv_string()
            print("Received message '{m}'".format(m=message))
    finally:
        print("Trying to close socket...")
        socket.close()
        print("Trying to destroy context...")
        context.destroy()


start_client()
