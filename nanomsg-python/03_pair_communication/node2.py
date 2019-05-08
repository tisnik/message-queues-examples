from nanomsg import Socket, PAIR

URL = "ipc:///tmp/example3"

socket = Socket(PAIR)
print("Socket created")

socket.connect(URL)
print("Connected to URL {}".format(URL))

message = socket.recv()
print("Received: {}".format(message))

socket.close()
print("Socket closed")
