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

XREP_PORT = 5556
XREQ_PORT = 5557


@context()
@socket(zmq.XREP)
@socket(zmq.XREQ)
def create_queue(xrep_port, xreq_port, context, frontend, backend):
    """Vytvoření fronty."""
    zmq.Context()

    address = "tcp://*:{port}".format(port=xrep_port)
    frontend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=xrep_port))

    address = "tcp://*:{port}".format(port=xreq_port)
    backend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=xreq_port))

    zmq.device(zmq.QUEUE, frontend, backend)


create_queue(5556, 5557)
