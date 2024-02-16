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
