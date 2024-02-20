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
from time import sleep

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PUB
PORT = 5557


def bind(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://*:{port}".format(port=port)
    socket.bind(address)
    print("Bound to {a}".format(a=address))


def publish_message(socket, message):
    """Publikování zprávy zprávy."""
    print("Publishing message '{m}'".format(m=message))
    socket.send_string(message)


@context()
@socket(CONNECTION_TYPE)
def start_publisher(port, context, socket):
    """Spuštění publisheru."""
    pid = getpid()
    print("Publisher PID={pid}".format(pid=pid))

    bind(socket, port)
    for i in range(100):
        message = "Message #{i} from {pid}".format(i=i, pid=pid)
        publish_message(socket, message)
        sleep(0.3)


start_publisher(PORT)
