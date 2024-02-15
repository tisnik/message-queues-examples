import zmq
from zmq.decorators import context, socket

SUB_PORT = 5556
PUB_PORT = 5557


@context()
@socket(zmq.SUB)
@socket(zmq.PUB)
def create_queue(sub_port, pub_port, context, frontend, backend):
    """Vytvoření forwarderu."""
    zmq.Context()

    address = "tcp://*:{port}".format(port=sub_port)
    frontend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=sub_port))
    frontend.setsockopt_string(zmq.SUBSCRIBE, "")

    address = "tcp://*:{port}".format(port=pub_port)
    backend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=pub_port))

    zmq.device(zmq.FORWARDER, frontend, backend)


create_queue(SUB_PORT, PUB_PORT)
