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

from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container

ADDRESS = "localhost:5672"
TARGET = "queue://test"

MAX_MESSAGES = 1


class Publisher(MessagingHandler):
    def __init__(self, url, target):
        super(Publisher, self).__init__()
        self.url = url
        self.target = target
        self.message_sent = 0
        self.message_accepted = 0

    def on_start(self, event):
        print("on_start()")
        connection = event.container.connect(self.url)
        event.container.create_sender(connection, self.target)

    def on_sendable(self, event):
        print("on_sendable()")
        if self.message_sent < MAX_MESSAGES:
            self.message_sent += 1
            body = "Hello world #{n}".format(n=self.message_sent)
            message = Message(id=self.message_sent, body=body)
            event.sender.send(message)
            print("Message #{n} has been sent".format(n=self.message_sent))
        elif self.message_sent == MAX_MESSAGES:
            self.message_sent += 1
            message = Message(id=self.message_sent, body="exit")
            event.sender.send(message)
            print("Exit message")

    def on_accepted(self, event):
        print("on_accepted()")
        self.message_accepted += 1
        if self.message_accepted == self.message_sent:
            print("All messages confirmed")
            event.connection.close()
        print("Number of accepted messages: {n}".format(n=self.message_accepted))

    def on_disconnected(self, event):
        print("on_disconnected()")


publisher = Publisher(ADDRESS, TARGET)
container = Container(publisher)
container.run()
