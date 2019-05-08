from nanomsg import Socket, REP

URL = "ipc:///tmp/example7"


def receive_request(socket):
    request = socket.recv()
    print("Received request: '{}'".format(request))


def send_response(socket, response):
    socket.send(response)


# pocitadlo pozadavku
received = 0

with Socket(REP) as socket:
    print("Socket created")

    socket.bind(URL)
    print("Bound to URL {}".format(URL))

    print("Waiting for requests...")
    while True:
        receive_request(socket)
        received += 1
        print("Received {}th request".format(received))
        send_response(socket, "ACK!")

print("Socket closed")
