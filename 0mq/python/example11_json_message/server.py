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
from datetime import datetime

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def send_json_message(socket, message, i, timestamp):
    """Poslání zprávy."""
    print("Sending message #{i}'".format(i=i))
    payload = {"message": message, "number": i, "timestamp": str(timestamp)}
    socket.send_json(payload)


@context()
@socket(CONNECTION_TYPE)
def start_server(context, socket):
    """Spuštění serveru."""

    address = "tcp://*:{port}".format(port=PORT)
    socket.bind(address)
    print("Bound to address {a}".format(a=address))

    for i in range(10):
        send_json_message(socket, "Message", i, datetime.now())
        time.sleep(1)


start_server()
