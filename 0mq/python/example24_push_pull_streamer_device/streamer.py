import time

import zmq
from zmq.decorators import context, socket
from zmq.devices.basedevice import ProcessDevice

PULL_PORT = 5550
PUSH_PORT = 5551

PRODUCER_CONNECTION_TYPE = zmq.PUSH
PRODUCER_PORT = 5550


def create_streamer(pull_port, push_port):
    """Vytvoření streameru."""
    streamer_device = ProcessDevice(zmq.STREAMER, zmq.PULL, zmq.PUSH)

    frontend_address = "tcp://*:{port}".format(port=pull_port)
    backend_address = "tcp://*:{port}".format(port=push_port)

    streamer_device.bind_in(frontend_address)
    streamer_device.bind_out(backend_address)

    print("Bound to {a} on port {p}".format(a=frontend_address, p=pull_port))
    print("Bound to {a} on port {p}".format(a=backend_address, p=push_port))

    streamer_device.start()
    print("Device started in background")


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


@socket(PRODUCER_CONNECTION_TYPE)
def start_producer(port, context, socket):
    """Spuštění zdroje zprav."""

    address = "tcp://localhost:{port}".format(port=port)
    # socket.set_hwm(1)
    socket.connect(address)
    print("Connected to address {a}".format(a=address))

    for i in range(100):
        send_message(socket, "Message #{i}".format(i=i))
        time.sleep(0.2)


@context()
def start_device_and_producer(context):
    create_streamer(PULL_PORT, PUSH_PORT)
    start_producer(PRODUCER_PORT, context)


start_device_and_producer()
