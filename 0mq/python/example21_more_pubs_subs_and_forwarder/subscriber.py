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

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.SUB
PORT = 5557


def connect(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))


@context()
@socket(CONNECTION_TYPE)
def start_subscriber(port, context, socket):
    """Spuštění příjemce."""
    connect(socket, port)
    socket.setsockopt_string(zmq.SUBSCRIBE, "")

    print("Waiting for messages...")

    while True:
        message = socket.recv_string()
        print("Received message '{m}'".format(m=message))


start_subscriber(PORT)
