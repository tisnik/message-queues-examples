# vim: set fileencoding=utf-8

# Copyright © 2019 Pavel Tisnovsky
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
        answer = "Hello, I'm client #1. It must be {}".format(number)

        send_answer(socket, answer)
        print("Answer sent")

print("Socket closed")
