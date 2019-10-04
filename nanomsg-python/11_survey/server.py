# vim: set fileencoding=utf-8

from nanomsg import Socket, SURVEYOR
from time import sleep

URL = "ipc:///tmp/example11"


def send_survey(socket, message):
    socket.send(message)


def receive_answer(socket):
    answer = socket.recv()
    print("Received answer: '{}'".format(answer))


def wait_for_clients(seconds):
    print("Waiting for clients to connect...")
    for i in range(seconds, 0, -1):
        print(i)
        sleep(1)


with Socket(SURVEYOR) as socket:
    print("Socket created")

    socket.bind(URL)
    print("Bound to URL {}".format(URL))

    wait_for_clients(10)

    send_survey(socket, "What do you get when you multiply six by nine?")
    print("Survey send, waiting for answers...")

    answers = 0

    while True:
        receive_answer(socket)
        answers += 1
        print("Processed {} answers so far".format(answers))

print("Socket closed")
