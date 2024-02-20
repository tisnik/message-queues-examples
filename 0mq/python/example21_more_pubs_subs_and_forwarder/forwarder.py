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

SUB_PORT = 5556
PUB_PORT = 5557


@context()
@socket(zmq.SUB)
@socket(zmq.PUB)
def create_queue(sub_port, pub_port, context, frontend, backend):
    """Vytvoření forwarderu."""
    zmq.Context()

    address = "tcp://*:{port}".format(port=sub_port)
    frontend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=sub_port))
    frontend.setsockopt_string(zmq.SUBSCRIBE, "")

    address = "tcp://*:{port}".format(port=pub_port)
    backend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=pub_port))

    zmq.device(zmq.FORWARDER, frontend, backend)


create_queue(SUB_PORT, PUB_PORT)
