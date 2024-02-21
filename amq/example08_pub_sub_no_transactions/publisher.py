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

destination1 = "/topic/event"
destination2 = "/topic/event2"

MESSAGES = 10

conn = stomp.Connection([("localhost", 61613)])
conn.start()
conn.connect(login="admin", passcode="admin")


for i in range(0, MESSAGES):
    message = "Hello world #{i}!".format(i=i)
    print("Publishing message: " + message)
    conn.send(destination1, message, persistent="true")
    conn.send(destination2, message, persistent="true")
    time.sleep(1)
    print("Done")


conn.disconnect()
