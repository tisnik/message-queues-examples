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

from rabbitmq_connect import connect, open_channel


def run_producer(queue_name):
    connection = connect()
    channel = open_channel(connection)

    for i in range(1, 11):
        channel.basic_publish(
            exchange="", routing_key=queue_name, body="Hello World! #{i}".format(i=i)
        )

    print("Sent 'Hello World!' ten times into the queue \"{q}\"".format(q=queue_name))
    connection.close()


run_producer("test")
