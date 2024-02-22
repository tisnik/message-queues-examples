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

from nanomsg import PAIR, Socket

URL = "ipc:///tmp/example4"

socket = Socket(PAIR)
print("Socket created")

socket.connect(URL)
print("Connected to URL {}".format(URL))

message = socket.recv()
print("Received: {}".format(message))

socket.send("Thanks for your message '{}'".format(message))
print("Response has been sent")

socket.close()
print("Socket closed")
