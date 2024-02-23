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

from sys import argv, exit
from time import sleep

from rabbitmq_connect import connect, open_channel


def on_receive(ch, method, properties, body):
    print("Received %r" % body)
    sleep(0.2)
    print("Done processing %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def run_consumer(queue_name):
    connection = connect()
    channel = open_channel(connection, queue_name, max_priority=100)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_receive, queue=queue_name, no_ack=False)
    print(
        'Waiting for messages in queue "{q}". To exit press CTRL+C'.format(q=queue_name)
    )
    print("...")
    channel.start_consuming()


if len(argv) <= 1:
    print("Please provide queue name on the CLI")
    exit(1)

run_consumer(argv[1])
