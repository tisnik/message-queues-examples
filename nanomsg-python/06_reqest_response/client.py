from nanomsg import Socket, REQ

URL = "ipc:///tmp/example6"


def send_request(socket, request):
    socket.send(request)


def receive_response(socket):
    response = socket.recv()
    print("Received response: '{}'".format(response))


with Socket(REQ) as socket:
    print("Socket created")

    socket.connect(URL)
    print("Connected to URL {}".format(URL))

    send_request(socket, "Hello from 'first'!")
    print("Waiting for response...")
    receive_response(socket)

print("Socket closed")
