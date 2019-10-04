# vim: set fileencoding=utf-8

from nanomsg import Socket, PAIR

URL = "ipc:///tmp/example5"

with Socket(PAIR) as socket:
    socket = Socket(PAIR)
    print("Socket created")

    socket.connect(URL)
    print("Connected to URL {}".format(URL))

    message = socket.recv()
    print("Received: {}".format(message))

    socket.send("Thanks for your message '{}'".format(message))
    print("Response has been sent")

print("Socket closed")
