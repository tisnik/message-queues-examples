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

from time import sleep

from rabbitmq_connect import connect

connection, channel = connect()


def on_receive(ch, method, properties, body):
    print("Received %r" % body)
    sleep(5)
    print("Done processing %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_receive, queue="test", no_ack=False)

print("Waiting for messages. To exit press CTRL+C")
print("...")
channel.start_consuming()
