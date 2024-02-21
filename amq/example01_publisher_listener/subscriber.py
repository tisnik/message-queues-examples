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

import time

import stomp


class SimpleListener:
    def __init__(self, conn):
        self.conn = conn

    def on_message(self, headers, message):
        print("Received message: {m}".format(m=message))

    def on_error(self, headers, message):
        print("Received an error {e}".format(e=message))


destination = "/topic/event"

conn = stomp.Connection(host_and_ports=[("localhost", 61613)])
conn.set_listener("", SimpleListener(conn))
conn.start()

conn.connect(login="admin", passcode="admin")
conn.subscribe(id="simple_listener", destination=destination, ack="auto")

print("Waiting for messages...")

while True:
    time.sleep(10)
