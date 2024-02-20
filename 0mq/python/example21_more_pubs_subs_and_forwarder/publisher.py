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

from sys import argv, exit
from time import sleep

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PUB
PORT = 5556


def connect(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))


def publish_message(socket, message):
    """Publikování zprávy zprávy."""
    print("Publishing message '{m}'".format(m=message))
    socket.send_string(message)


@context()
@socket(CONNECTION_TYPE)
def start_publisher(name, delay, port, context, socket):
    """Spuštění publisheru."""
    print("Publisher '{name}'".format(name=name))

    connect(socket, port)
    for i in range(100):
        message = "Message #{i} from {name}".format(i=i, name=name)
        publish_message(socket, message)
        sleep(delay)


if len(argv) <= 2:
    print("Please provide publisher name and sleep amount on the CLI")
    exit(1)


name = argv[1]
delay = float(argv[2])
start_publisher(name, delay, PORT)
