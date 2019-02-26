from proton.handlers import MessagingHandler
from proton.reactor import Container

ADDRESS = "localhost:5672"


class Subscriber(MessagingHandler):

    def __init__(self, url):
        super(Subscriber, self).__init__()
        self.url = url
        self.target = target

    def on_start(self, event):
        print("on_start()")
        connection = event.container.connect(self.url)
        event.container.create_receiver(connection, "topic://")

    def on_message(self, event):
        message = event.message

        print(message.body)


subscriber = Subscriber(ADDRESS)
container = Container(subscriber)
container.run()
