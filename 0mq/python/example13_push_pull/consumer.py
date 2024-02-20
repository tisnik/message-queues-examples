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

import time

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PULL
PORT = 5556


@context()
@socket(CONNECTION_TYPE)
def start_consumer(context, socket):
    """Spuštění konzumenta."""

    address = "tcp://localhost:{port}".format(port=PORT)
    socket.connect(address)
    print("Connected to {a}".format(a=address))

    print("Waiting for message...")
    cnt = 0
    while True:
        message = socket.recv_string()
        cnt += 1
        print("Received message {c} of 100: '{m}'".format(c=cnt, m=message))
        time.sleep(0)


start_consumer()
