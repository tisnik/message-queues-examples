import zmq
from zmq.decorators import context, socket

PULL_PORT = 5550
PUSH_PORT = 5551


@context()
@socket(zmq.PULL)
@socket(zmq.PUSH)
def create_streamer(pull_port, push_port, context, frontend, backend):
    """Vytvoření streameru."""
    zmq.Context()

    address = "tcp://*:{port}".format(port=pull_port)
    frontend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=pull_port))

    address = "tcp://*:{port}".format(port=push_port)
    backend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=push_port))

    zmq.device(zmq.STREAMER, frontend, backend)


create_streamer(PULL_PORT, PUSH_PORT)
