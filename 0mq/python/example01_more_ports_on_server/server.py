import time

import zmq


def bind(port1, port2, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address1 = "tcp://*:{port}".format(port=port1)
    socket.bind(address1)
    print("Bound to address {a}".format(a=address1))
    address2 = "tcp://*:{port}".format(port=port2)
    socket.bind(address2)
    print("Bound to address {a}".format(a=address2))
    return socket


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


def start_server():
    """Spuštění serveru."""
    socket = bind(5556, 5557, zmq.PAIR)
    for i in range(10):
        send_message(socket, "Message #{i}".format(i=i))
        time.sleep(1)


start_server()
