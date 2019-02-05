# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu PyZMQ založenou na 0MQ.
#
# Příklad číslo 5: obousměrně komunikující klient s komunikační strategií REQ-REP.
#
# ---------------------------------------------------------------------

import zmq


def connect(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))
    return socket


def send_request(socket, request):
    """Poslání požadavku."""
    print("Sending request '{r}'".format(r=request))
    socket.send_string(request)


def start_client():
    """Spuštění klienta."""
    socket = connect(5555, zmq.REQ)

    send_request(socket, "1")
    print(socket.recv_string())
    print()

    send_request(socket, "10")
    print(socket.recv_string())
    print()

    send_request(socket, "xyzzy")
    print(socket.recv_string())
    print()


start_client()
