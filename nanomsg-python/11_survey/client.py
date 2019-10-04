# vim: set fileencoding=utf-8

from nanomsg import Socket, RESPONDENT
from random import seed, randint

URL = "ipc:///tmp/example11"


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
        answer = "It must be {}".format(number)

        send_answer(socket, answer)
        print("Answer sent")

print("Socket closed")
