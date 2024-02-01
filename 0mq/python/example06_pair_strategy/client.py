# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu PyZMQ založenou na 0MQ.
#
# Příklad číslo 6: klient s komunikační strategií PAIR.
#
# ---------------------------------------------------------------------

import zmq

CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def start_client():
    """Spuštění klienta."""
    context = zmq.Context()

    socket = context.socket(CONNECTION_TYPE)
    address = "tcp://localhost:{port}".format(port=PORT)
    socket.connect(address)
    print("Connected to {a}".format(a=address))

    print("Waiting for message...")
    while True:
        message = socket.recv_string()
        print("Received message '{m}'".format(m=message))


start_client()
