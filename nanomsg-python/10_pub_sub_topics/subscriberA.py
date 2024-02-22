# vim: set fileencoding=utf-8

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


from nanomsg import SUB, SUB_SUBSCRIBE, Socket

URL = "ipc:///tmp/example10"


def receive_message(socket):
    message = socket.recv()
    print("Received message: '{}'".format(message))


with Socket(SUB) as socket:
    print("Socket created")

    socket.connect(URL)
    socket.set_string_option(SUB, SUB_SUBSCRIBE, "Message A")
    print("Connected to URL {}".format(URL))

    while True:
        receive_message(socket)

print("Socket closed")
