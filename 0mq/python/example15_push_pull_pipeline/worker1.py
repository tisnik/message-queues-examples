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

from os import getpid

import zmq
from zmq.decorators import context, socket

IN_PORT = 5556
OUT_PORT = 5557


@context()
@socket(zmq.PULL)
@socket(zmq.PUSH)
def start_worker(context, in_socket, out_socket):
    """Spuštění workera."""

    address = "tcp://localhost:{port}".format(port=IN_PORT)
    in_socket.connect(address)
    print("Connected to {a}".format(a=address))

    address = "tcp://*:{port}".format(port=OUT_PORT)
    out_socket.bind(address)
    print("And to {a}".format(a=address))

    print("Waiting for message from producer...")
    pid = getpid()

    while True:
        message = in_socket.recv_string()
        out_message = "Message from {pid}: '{m}'".format(pid=pid, m=message)
        print(out_message)
        out_socket.send_string(out_message)


start_worker()
