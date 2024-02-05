from math import factorial

import zmq
from zmq.decorators import context
from zmq.devices.basedevice import ProcessDevice

XREP_PORT = 5556
XREQ_PORT = 5557

SERVER_PORT = 5557


def create_queue(xrep_port, xreq_port):
    """Vytvoření fronty."""
    queue_device = ProcessDevice(zmq.QUEUE, zmq.XREP, zmq.XREQ)

    frontend_address = "tcp://*:{port}".format(port=xrep_port)
    backend_address = "tcp://*:{port}".format(port=xreq_port)

    queue_device.bind_in(frontend_address)
    queue_device.bind_out(backend_address)

    print("Bound to {a} on port {p}".format(a=frontend_address, p=xrep_port))
    print("Bound to {a} on port {p}".format(a=backend_address, p=xreq_port))

    queue_device.start()
    print("Queue device started in background")


def connect(context, port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
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


def start_server(context, port):
    """Spuštění serveru."""
    socket = connect(context, port, zmq.REP)
    while True:
        request = receive_request(socket)
        try:
            n = int(request)
            fact = factorial(n)
            send_response(socket, "{n}! = {f}".format(n=n, f=fact))
        except Exception as e:
            send_response(socket, "Wrong input")


@context()
def start_device_and_server(context):
    create_queue(XREP_PORT, XREQ_PORT)
    start_server(context, SERVER_PORT)


start_device_and_server()
