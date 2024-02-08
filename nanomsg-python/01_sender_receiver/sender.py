# vim: set fileencoding=utf-8

from nanomsg import PUSH, Socket

URL = "ipc:///tmp/example1"

socket = Socket(PUSH)
print("Socket created")

socket.connect(URL)
print("Connected to URL {}".format(URL))

socket.send("Hello world!")
print("Message has been sent")

socket.close()
print("Socket closed")
