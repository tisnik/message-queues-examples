from nanomsg import Socket, PULL

URL = "ipc:///tmp/example2"

socket = Socket(PULL)
print("Socket created")

socket.bind(URL)
print("Bound to URL {}".format(URL))

while True:
    message = socket.recv()
    print("Received: {}".format(message))

socket.close()
print("Socket closed")
