# vim: set fileencoding=utf-8

from nanomsg import PAIR, Socket

URL = "ipc:///tmp/example5"

with Socket(PAIR) as socket:
    print("Socket created")

    socket.bind(URL)
    print("Bound to URL {}".format(URL))

    socket.send("Hello world!")
    print("Message has been sent")

    message = socket.recv()
    print("Received response: {}".format(message))

print("Socket closed")
