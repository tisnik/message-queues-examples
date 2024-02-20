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

PULL_PORT = 5550
PUSH_PORT = 5551


@context()
@socket(zmq.PULL)
@socket(zmq.PUSH)
def create_streamer(pull_port, push_port, context, frontend, backend):
    """Vytvoření streameru."""
    zmq.Context()

    address = "tcp://*:{port}".format(port=pull_port)
    frontend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=pull_port))

    address = "tcp://*:{port}".format(port=push_port)
    backend.bind(address)
    print("Bound to {a} on port {p}".format(a=address, p=push_port))

    zmq.device(zmq.STREAMER, frontend, backend)


create_streamer(PULL_PORT, PUSH_PORT)
