import zmq
import time


CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


def start_server():
    """Spuštění serveru."""

    with zmq.Context() as context:
        with context.socket(CONNECTION_TYPE) as socket:
            address = "tcp://*:{port}".format(port=PORT)
            socket.bind(address)
            print("Bound to address {a}".format(a=address))

            for i in range(10):
                send_message(socket, "Message #{i}".format(i=i))
                time.sleep(1)


start_server()
