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

from rabbitmq_connect import connect


def delete_queue(queue_name):
    connection = connect()
    channel = connection.channel()
    channel.queue_delete(queue=queue_name)
    connection.close()


if len(argv) <= 1:
    print("Please provide queue name on the CLI")
    exit(1)

delete_queue(argv[1])
