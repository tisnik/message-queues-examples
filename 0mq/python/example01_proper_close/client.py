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


def connect(port, connection_type):
    """Otevření socketu se specifikovaným typem spojení."""
    context = zmq.Context()
    socket = context.socket(connection_type)
    address = "tcp://localhost:{port}".format(port=port)
    socket.connect(address)
    print("Connected to {a}".format(a=address))
    return context, socket


def start_client():
    """Spuštění klienta."""
    try:
        context, socket = connect(5556, zmq.PAIR)
        print("Waiting for messages...")
        while True:
            message = socket.recv_string()
            print("Received message '{m}'".format(m=message))
    finally:
        print("Trying to close socket...")
        socket.close()
        print("Trying to destroy context...")
        context.destroy()


start_client()
