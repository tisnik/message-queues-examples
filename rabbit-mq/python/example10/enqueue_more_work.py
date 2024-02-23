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


from rabbitmq_connect import bind_queue, connect, open_channel, use_topic_exchange


def run_producer():
    connection = connect()
    channel = open_channel(connection)

    use_topic_exchange(channel)
    bind_queue(
        channel,
        "europe_queue",
        routing_pattern="europe.*",
        exchange_name="topic_exchange",
    )
    bind_queue(
        channel, "asia_queue", routing_pattern="asia.*", exchange_name="topic_exchange"
    )
    bind_queue(
        channel,
        "americas_queue",
        routing_pattern="americas.*",
        exchange_name="topic_exchange",
    )

    keys = (
        "europe.cr",
        "europe.sr",
        "europe.pl",
        "asia.china",
        "americas.canada",
        "americas.chile",
    )
    for key in keys:
        print(key)
        channel.basic_publish(
            exchange="topic_exchange",
            routing_key=key,
            body="Hello World! #{k}".format(k=key),
        )

    print("Sent 'Hello World!' to all selected regions")
    connection.close()


run_producer()
