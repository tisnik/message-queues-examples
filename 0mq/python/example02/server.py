# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu PyZMQ založenou na 0MQ.
#
# Příklad číslo 2: obousměrně komunikující server s komunikační strategií PAIR.
#
# ---------------------------------------------------------------------

import time

import zmq


def bind(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://*:{port}".format(port=port)
    socket.bind(address)
    print("Bound to address {a}".format(a=address))
    return socket


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


def receive_response(socket):
    """Zpracování odpovědi klienta."""
    response = socket.recv_string()
    print("Received response from client: '{r}'".format(r=response))


def start_server():
    """Spuštění serveru."""
    socket = bind(5556, zmq.PAIR)
    for i in range(10):
        send_message(socket, "Message #{i}".format(i=i))
        print("Sent, waiting for response...")
        receive_response(socket)
        time.sleep(1)
        print()


start_server()
