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

from nanomsg import REP, Socket

URL = "ipc:///tmp/example7"


def receive_request(socket):
    request = socket.recv()
    print("Received request: '{}'".format(request))


def send_response(socket, response):
    socket.send(response)


# pocitadlo pozadavku
received = 0

with Socket(REP) as socket:
    print("Socket created")

    socket.bind(URL)
    print("Bound to URL {}".format(URL))

    print("Waiting for requests...")
    while True:
        receive_request(socket)
        received += 1
        print("Received {}th request".format(received))
        send_response(socket, "ACK!")

print("Socket closed")
