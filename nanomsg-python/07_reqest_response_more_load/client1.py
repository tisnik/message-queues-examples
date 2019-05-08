from nanomsg import Socket, REQ

URL = "ipc:///tmp/example7"


def send_request(socket, request):
    socket.send(request)


def receive_response(socket):
    response = socket.recv()
    print("Received response: '{}'".format(response))


with Socket(REQ) as socket:
    print("Socket created")

    socket.connect(URL)
    print("Connected to URL {}".format(URL))

    for i in range(1000):
        send_request(socket, "Hello #{} from 'first'!".format(i))
        print("Waiting for response...")
        receive_response(socket)

print("Socket closed")
