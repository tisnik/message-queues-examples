import zmq
import time


def bind(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://*:{port}".format(port=port)
    socket.bind(address)
    print("Bound to address {a}".format(a=address))
    return context, socket


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


def start_server():
    """Spuštění serveru."""
    context, socket = bind(5556, zmq.PAIR)
    try:
        for i in range(10):
            send_message(socket, "Message #{i}".format(i=i))
            time.sleep(1)
    finally:
        print("Trying to close socket...")
        socket.close()
        print("Trying to destroy context...")
        context.destroy()


start_server()
