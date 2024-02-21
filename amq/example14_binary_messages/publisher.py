#!/usr/bin/env python

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

import base64

import stomp

destination = "/queue/test"

conn = stomp.Connection(host_and_ports=[("localhost", 61613)])
conn.start()
conn.connect(login="admin", passcode="admin")


with open("vim_editor.gif", mode="rb") as file:
    binaryData = file.read()
    print("Read {length} bytes from binary file".format(length=len(binaryData)))

    textData = base64.b64encode(binaryData)
    conn.send(destination, textData, persistent="true")
    print("Sent {length} characters".format(length=len(textData)))


conn.disconnect()
