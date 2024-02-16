from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container

ADDRESS = "localhost:5672"
TARGET = "queue://test"


class Publisher(MessagingHandler):
    def __init__(self, url, target):
        super(Publisher, self).__init__()
        self.url = url
        self.target = target
        self.message_sent = False

    def on_start(self, event):
        print("on_start()")
        connection = event.container.connect(self.url)
        event.container.create_sender(connection, self.target)

    def on_sendable(self, event):
        print("on_sendable()")
        if not self.message_sent:
            message = Message(id=1, body="Hello world1")
            event.sender.send(message)
            self.message_sent = True
            print("Message has been sent")
        else:
            print("Already sent... do nothing")

    def on_accepted(self, event):
        print("on_accepted()")
        if self.message_sent:
            event.connection.close()

    def on_disconnected(self, event):
        print("on_disconnected()")


publisher = Publisher(ADDRESS, TARGET)
container = Container(publisher)
container.run()
