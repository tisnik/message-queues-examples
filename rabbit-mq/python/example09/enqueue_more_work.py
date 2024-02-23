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


from rabbitmq_connect import bind_queue, connect, open_channel, use_fanout


def run_producer():
    connection = connect()
    channel = open_channel(connection)

    use_fanout(channel)
    bind_queue(channel, "fronta1")
    bind_queue(channel, "fronta2")
    bind_queue(channel, "fronta3")

    for i in range(1, 11):
        channel.basic_publish(
            exchange="fanout_exchange",
            routing_key="",
            body="Hello World! #{i}".format(i=i),
        )

    print(
        'Sent \'Hello World!\' ten times into three queues "fronta1", "fronta2", and "fronta3"'
    )
    connection.close()


run_producer()
