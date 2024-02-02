from math import factorial

import zmq

PORT = 5557


def connect(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))
    return socket


def send_response(socket, response):
    """Odeslání odpovědi."""
    print("Sending response '{r}'".format(r=response))
    socket.send_string(response)


def receive_request(socket):
    """Zpracování požadavku klienta."""
    request = socket.recv_string()
    print("Received request from client: '{r}'".format(r=request))
    return request


def start_server():
    """Spuštění serveru."""
    socket = connect(PORT, zmq.REP)
    while True:
        request = receive_request(socket)
        try:
            n = int(request)
            fact = factorial(n)
            send_response(socket, "{n}! = {f}".format(n=n, f=fact))
        except Exception as e:
            send_response(socket, "Wrong input")


start_server()
