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

from proton.handlers import MessagingHandler
from proton.reactor import Container

ADDRESS = "localhost:5672"

TOPICS = (
    "ActiveMQ.Advisory.Connection",
    "ActiveMQ.Advisory.Consumer.Queue.test",
    "ActiveMQ.Advisory.MasterBroker",
    "ActiveMQ.Advisory.Producer.Queue.test",
    "ActiveMQ.Advisory.Queue",
    "ActiveMQ.Advisory.Topic",
)


class Subscriber(MessagingHandler):
    def __init__(self, url):
        super(Subscriber, self).__init__()
        self.url = url

    def on_start(self, event):
        print("on_start()")
        connection = event.container.connect(self.url)
        for topic in TOPICS:
            event.container.create_receiver(connection, "topic://" + topic)

    def on_message(self, event):
        message = event.message
        print(message)


subscriber = Subscriber(ADDRESS)
container = Container(subscriber)
container.run()
