# vim: set fileencoding=utf-8

from time import sleep

from nanomsg import PUB, Socket

URL = "ipc:///tmp/example8"


with Socket(PUB) as socket:
    print("Socket created")

    socket.bind(URL)
    print("Bound to URL {}".format(URL))

    for i in range(1, 1000):
        message = "Message #{}".format(i)
        print("Publishing message {}".format(message))
        socket.send(message)
        sleep(0.5)

print("Socket closed")
