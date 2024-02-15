import zmq
from zmq.decorators import context, socket

XREP_PORT = 5556
XREQ_PORT = 5557


@context()
@socket(zmq.XREP)
@socket(zmq.XREQ)
def create_queue(xrep_port, xreq_port, context, frontend, backend):
    """Vytvoření fronty."""
    zmq.Context()

    address = "tcp://*:{port}".format(port=xrep_port)
    frontend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=xrep_port))

    address = "tcp://*:{port}".format(port=xreq_port)
    backend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=xreq_port))

    zmq.device(zmq.QUEUE, frontend, backend)


create_queue(5556, 5557)
