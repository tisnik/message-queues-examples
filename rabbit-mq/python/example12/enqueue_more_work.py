#!/usr/bin/env python
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


from pika.spec import BasicProperties
from rabbitmq_connect import connect, open_channel


def run_producer():
    connection = connect()
    channel = open_channel(connection, queue_name="priority_queue_3", max_priority=100)

    for i in range(0, 100):
        priority = 100 - i
        prop = BasicProperties(priority=priority)
        body = "Hello World! #{i} msg with priority {p}".format(i=i, p=priority)
        channel.basic_publish(
            exchange="", routing_key="priority_queue_3", body=body, properties=prop
        )

    connection.close()


run_producer()
