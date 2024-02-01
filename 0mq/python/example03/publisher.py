# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu PyZMQ založenou na 0MQ.
#
# Příklad číslo 3: publisher (zdroj zpráv) používající komunikační strategii PUB-SUB.
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
    print("Publishing message '{m}'".format(m=message))
    socket.send_string(message)


def start_publisher():
    """Spuštění publisheru."""
    socket = bind(5556, zmq.PUB)
    for i in range(10):
        send_message(socket, "Message #{i}".format(i=i))
        time.sleep(1)


start_publisher()
