# vim: set fileencoding=utf-8

from nanomsg import PULL, Socket

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
