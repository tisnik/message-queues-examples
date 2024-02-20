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
from zmq.decorators import context, socket
from zmq.devices.basedevice import ProcessDevice

PULL_PORT = 5550
PUSH_PORT = 5551

PRODUCER_CONNECTION_TYPE = zmq.PUSH
PRODUCER_PORT = 5550


def create_streamer(pull_port, push_port):
    """Vytvoření streameru."""
    streamer_device = ProcessDevice(zmq.STREAMER, zmq.PULL, zmq.PUSH)

    frontend_address = "tcp://*:{port}".format(port=pull_port)
    backend_address = "tcp://*:{port}".format(port=push_port)

    streamer_device.bind_in(frontend_address)
    streamer_device.bind_out(backend_address)

    print("Bound to {a} on port {p}".format(a=frontend_address, p=pull_port))
    print("Bound to {a} on port {p}".format(a=backend_address, p=push_port))

    streamer_device.start()
    print("Device started in background")


def send_message(socket, message):
    """Poslání zprávy."""
    print("Sending message '{m}'".format(m=message))
    socket.send_string(message)


@socket(PRODUCER_CONNECTION_TYPE)
def start_producer(port, context, socket):
    """Spuštění zdroje zprav."""

    address = "tcp://localhost:{port}".format(port=port)
    # socket.set_hwm(1)
    socket.connect(address)
    print("Connected to address {a}".format(a=address))

    for i in range(100):
        send_message(socket, "Message #{i}".format(i=i))
        time.sleep(0.2)


@context()
def start_device_and_producer(context):
    create_streamer(PULL_PORT, PUSH_PORT)
    start_producer(PRODUCER_PORT, context)


start_device_and_producer()
