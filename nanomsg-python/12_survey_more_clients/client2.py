# vim: set fileencoding=utf-8

from random import randint, seed

from nanomsg import RESPONDENT, Socket

URL = "ipc:///tmp/example12"


def receive_question(socket):
    question = socket.recv()
    print("Received question: '{}'".format(question))


def send_answer(socket, answer):
    print("Sending answer: '{}'".format(answer))
    socket.send(answer)


seed(None)

with Socket(RESPONDENT) as socket:
    print("Socket created")

    socket.connect(URL)
    print("Connected to URL {}".format(URL))

    while True:
        receive_question(socket)
        print("Question received")

        number = randint(0, 100)
        answer = "Hello, I'm client #2. It must be {}".format(number)

        send_answer(socket, answer)
        print("Answer sent")

print("Socket closed")
