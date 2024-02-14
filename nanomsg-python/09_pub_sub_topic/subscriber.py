# vim: set fileencoding=utf-8


from nanomsg import SUB, SUB_SUBSCRIBE, Socket

URL = "ipc:///tmp/example9"


def receive_message(socket):
    message = socket.recv()
    print("Received message: '{}'".format(message))


with Socket(SUB) as socket:
    print("Socket created")

    socket.connect(URL)
    socket.set_string_option(SUB, SUB_SUBSCRIBE, "")
    print("Connected to URL {}".format(URL))

    while True:
        receive_message(socket)

print("Socket closed")
