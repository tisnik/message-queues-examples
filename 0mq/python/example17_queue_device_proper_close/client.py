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

CONNECTION_TYPE = zmq.REQ
PORT = 5556


def connect(socket, port):
    """Otevření socketu se specifikovaným typem spojení."""
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))


def send_request(socket, request):
    """Poslání požadavku."""
    print("Sending request '{r}'".format(r=request))
    socket.send_string(request)


@context()
@socket(CONNECTION_TYPE)
def start_client(port, context, socket):
    """Spuštění klienta."""
    connect(socket, port)

    send_request(socket, "1")
    print(socket.recv_string())
    print()

    send_request(socket, "10")
    print(socket.recv_string())
    print()

    send_request(socket, "xyzzy")
    print(socket.recv_string())
    print()

    send_request(socket, "-10")
    print(socket.recv_string())
    print()

    send_request(socket, "100")
    print(socket.recv_string())
    print()


start_client(PORT)
