from nanomsg import Socket, PAIR

URL = "ipc:///tmp/example4"

socket = Socket(PAIR)
print("Socket created")

socket.bind(URL)
print("Bound to URL {}".format(URL))

socket.send("Hello world!")
print("Message has been sent")

message = socket.recv()
print("Received response: {}".format(message))

socket.close()
print("Socket closed")
