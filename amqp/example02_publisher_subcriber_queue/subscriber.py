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

        event.receiver.close()
        event.connection.close()


subscriber = Subscriber(ADDRESS, SOURCE)
container = Container(subscriber)
container.run()
