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

CONNECTION_TYPE = zmq.PAIR
PORT = 5556


def start_client():
    """Spuštění klienta."""
    context = zmq.Context()

    try:
        socket = context.socket(CONNECTION_TYPE)
        address = "tcp://localhost:{port}".format(port=PORT)
        socket.connect(address)
        try:
            print("Connected to {a}".format(a=address))

            print("Waiting for message...")
            while True:
                message = socket.recv_string()
                print("Received message '{m}'".format(m=message))
        except Exception as e:
            print(e)
        finally:
            print("Closing socket")
            socket.close()
            print("Closed")
    except Exception as e:
        print(e)
    finally:
        print("Terminating context")
        context.term()
        print("Terminated")


start_client()
