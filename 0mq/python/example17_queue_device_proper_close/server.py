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

from math import factorial

import zmq
from zmq.decorators import context, socket

CONNECTION_TYPE = zmq.REP
PORT = 5557


def connect(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))


def send_response(socket, response):
    """Odeslání odpovědi."""
    print("Sending response '{r}'".format(r=response))
    socket.send_string(response)


def receive_request(socket):
    """Zpracování požadavku klienta."""
    request = socket.recv_string()
    print("Received request from client: '{r}'".format(r=request))
    return request


@context()
@socket(CONNECTION_TYPE)
def start_server(port, context, socket):
    """Spuštění serveru."""
    connect(socket, port)
    while True:
        request = receive_request(socket)
        try:
            n = int(request)
            fact = factorial(n)
            send_response(socket, "{n}! = {f}".format(n=n, f=fact))
        except Exception:
            send_response(socket, "Wrong input")


start_server(PORT)
