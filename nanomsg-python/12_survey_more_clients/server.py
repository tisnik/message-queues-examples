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

from time import sleep

from nanomsg import SURVEYOR, Socket

URL = "ipc:///tmp/example12"


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
