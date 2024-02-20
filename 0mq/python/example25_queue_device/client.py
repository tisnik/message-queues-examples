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

PORT = 5556


def connect(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))
    return socket


def send_request(socket, request):
    """Poslání požadavku."""
    print("Sending request '{r}'".format(r=request))
    socket.send_string(request)


def start_client():
    """Spuštění klienta."""
    socket = connect(PORT, zmq.REQ)

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


start_client()
