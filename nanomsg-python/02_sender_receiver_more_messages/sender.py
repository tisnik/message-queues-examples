# vim: set fileencoding=utf-8

from nanomsg import Socket, PUSH
from time import sleep

URL = "ipc:///tmp/example2"

socket = Socket(PUSH)
print("Socket created")

socket.connect(URL)
print("Connected to URL {}".format(URL))

for i in range(10):
    socket.send("Hello world #{}".format(i+1))
    print("Message has been sent")
    sleep(0.1)

socket.close()
print("Socket closed")
