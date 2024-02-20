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
from zmq.decorators import context

CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


@context()
def start_server(context):
    """Spuštění serveru."""

    with context.socket(CONNECTION_TYPE) as socket:
        address = "tcp://*:{port}".format(port=PORT)
        socket.bind(address)
        print("Bound to address {a}".format(a=address))

        for i in range(10):
            send_message(socket, "Message #{i}".format(i=i))
            time.sleep(1)


start_server()
