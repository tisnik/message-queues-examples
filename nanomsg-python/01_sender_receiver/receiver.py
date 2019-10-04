# vim: set fileencoding=utf-8

from nanomsg import Socket, PULL

URL = "ipc:///tmp/example1"

socket = Socket(PULL)
print("Socket created")

socket.bind(URL)
print("Bound to URL {}".format(URL))

message = socket.recv()
print("Received: {}".format(message))

socket.close()
print("Socket closed")
