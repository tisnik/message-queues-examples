import zmq

XREP_PORT = 5556
XREQ_PORT = 5557


def create_queue(xrep_port, xreq_port):
    """Vytvoření fronty."""
    context = zmq.Context()

    frontend = context.socket(zmq.XREP)
    address = "tcp://*:{port}".format(port=xrep_port)
    frontend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=xrep_port))

    backend = context.socket(zmq.XREQ)
    address = "tcp://*:{port}".format(port=xreq_port)
    backend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=xreq_port))

    zmq.device(zmq.QUEUE, frontend, backend)


create_queue(XREP_PORT, XREQ_PORT)
