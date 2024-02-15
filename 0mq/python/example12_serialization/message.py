from datetime import datetime


class Message:
    def __init__(self, number):
        self.number = number
        self.timestamp = str(datetime.now())
        self.message = "Message"
