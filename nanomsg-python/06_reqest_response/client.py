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

from nanomsg import REQ, Socket

URL = "ipc:///tmp/example6"


def send_request(socket, request):
    socket.send(request)


def receive_response(socket):
    response = socket.recv()
    print("Received response: '{}'".format(response))


with Socket(REQ) as socket:
    print("Socket created")

    socket.connect(URL)
    print("Connected to URL {}".format(URL))

    send_request(socket, "Hello from 'first'!")
    print("Waiting for response...")
    receive_response(socket)

print("Socket closed")
