import zmq
from zmq.decorators import context, socket
from time import sleep


CONNECTION_TYPE = zmq.PULL
PORT = 5558


@context()
@socket(CONNECTION_TYPE)
def start_collector(context, socket):
    """Spuštění sběratele."""

    address = "tcp://*:{port}".format(port=PORT)
    socket.bind(address)
    print("Connected to {a}".format(a=address))

    print("Waiting for message from worker #2 ...")
    while True:
        message = socket.recv_string()
        print("Collecting message: '{m}'".format(m=message))
        sleep(0)


start_collector()
