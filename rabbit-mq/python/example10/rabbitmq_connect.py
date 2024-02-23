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

import pika


def connect(where="localhost"):
    return pika.BlockingConnection(pika.ConnectionParameters(where))


def open_channel(connection, queue_name="test"):
    # pokus o nove vytvoreni fronty ve skutecnosti neovlivni jiz existujici frontu
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    return channel


def use_fanout(channel, exchange_name="fanout_exchange"):
    channel.exchange_declare(exchange=exchange_name, exchange_type="fanout")


def use_topic_exchange(channel, exchange_name="topic_exchange"):
    channel.exchange_declare(exchange=exchange_name, exchange_type="topic")


def bind_queue(
    channel, queue_name, routing_pattern="", exchange_name="fanout_exchange"
):
    channel.queue_declare(queue=queue_name)
    channel.queue_bind(
        exchange=exchange_name, queue=queue_name, routing_key=routing_pattern
    )
