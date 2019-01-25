import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.REQ
PORT = 5556


def connect(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))


def send_request(socket, request):
    """Poslání požadavku."""
    print("Sending request '{r}'".format(r=request))
    socket.send_string(request)


@context()
@socket(CONNECTION_TYPE)
def start_client(port, context, socket):
    """Spuštění klienta."""
    connect(socket, port)

    send_request(socket, "1")
    print(socket.recv_string())
    print()

    send_request(socket, "10")
    print(socket.recv_string())
    print()

    send_request(socket, "xyzzy")
    print(socket.recv_string())
    print()

    send_request(socket, "-10")
    print(socket.recv_string())
    print()

    send_request(socket, "100")
    print(socket.recv_string())
    print()


start_client(PORT)
