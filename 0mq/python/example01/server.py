import zmq
import time


def bind(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://*:{port}".format(port=port)
    socket.bind(address)
    return socket


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


def start_server():
    """Spuštění serveru."""
    socket = bind(5556, zmq.PAIR)
    for i in range(10):
        send_message(socket, "Message #{i}".format(i=i))
        time.sleep(1)


start_server()
