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
SOURCE = "queue://test"


class Subscriber(MessagingHandler):
    def __init__(self, url, source):
        super(Subscriber, self).__init__()
        self.url = url
        self.source = source

    def on_start(self, event):
        print("on_start()")
        connection = event.container.connect(self.url)
        event.container.create_receiver(connection, self.source)

    def on_message(self, event):
        message = event.message

        print("Received message '{m}'".format(m=message.body))

        if message.body == "exit":
            print("Last message for me...good bye")
            event.receiver.close()
            event.connection.close()


subscriber = Subscriber(ADDRESS, SOURCE)
container = Container(subscriber)
container.run()
