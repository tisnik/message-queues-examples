import zmq
from zmq.decorators import context, socket
import time
from datetime import datetime


CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def send_json_message(socket, message, i, timestamp):
    """Poslání zprávy."""
    print("Sending message #{i}'".format(i=i))
    payload = {
        "message": message,
        "number": i,
        "timestamp": str(timestamp)
    }
    socket.send_json(payload)


@context()
@socket(CONNECTION_TYPE)
def start_server(context, socket):
    """Spuštění serveru."""

    address = "tcp://*:{port}".format(port=PORT)
    socket.bind(address)
    print("Bound to address {a}".format(a=address))

    for i in range(10):
        send_json_message(socket, "Message", i, datetime.now())
        time.sleep(1)


start_server()
