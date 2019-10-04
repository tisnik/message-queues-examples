# vim: set fileencoding=utf-8

from nanomsg import Socket, PAIR

URL = "ipc:///tmp/example3"

socket = Socket(PAIR)
print("Socket created")

socket.bind(URL)
print("Bound to URL {}".format(URL))

socket.send("Hello world!")
print("Message has been sent")

socket.close()
print("Socket closed")
