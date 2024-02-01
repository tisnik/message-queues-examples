# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu PyZMQ založenou na 0MQ.
#
# Příklad číslo 5: obousměrně komunikující server s komunikační strategií REQ-REP.
#
# ---------------------------------------------------------------------

from math import factorial

import zmq


def bind(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://*:{port}".format(port=port)
    socket.bind(address)
    print("Bound to address {a}".format(a=address))
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
    socket = bind(5556, zmq.REP)
    while True:
        request = receive_request(socket)
        try:
            n = int(request)
            fact = factorial(n)
            send_response(socket, "{n}! = {f}".format(n=n, f=fact))
        except Exception as e:
            send_response(socket, "Wrong input")


start_server()
