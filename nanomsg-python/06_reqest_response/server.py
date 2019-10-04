# vim: set fileencoding=utf-8

from nanomsg import Socket, REP

URL = "ipc:///tmp/example6"


def receive_request(socket):
    request = socket.recv()
    print("Received request: '{}'".format(request))


def send_response(socket, response):
    socket.send(response)


with Socket(REP) as socket:
    print("Socket created")

    socket.bind(URL)
    print("Bound to URL {}".format(URL))

    print("Waiting for requests...")
    while True:
        receive_request(socket)
        send_response(socket, "ACK!")

print("Socket closed")
