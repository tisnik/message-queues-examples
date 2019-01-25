# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu PyZMQ založenou na 0MQ.
#
# Příklad číslo 2: obousměrně komunikující klient s komunikační strategií PAIR.
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


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


def start_client():
    """Spuštění klienta."""
    socket = connect(5556, zmq.PAIR)
    print("Waiting for messages...")
    while True:
        message = socket.recv_string()
        print(message)
        send_message(socket, "Acknowledge... " + message)


start_client()
