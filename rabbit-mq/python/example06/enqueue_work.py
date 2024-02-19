#!/usr/bin/env python
from rabbitmq_connect import connect, open_channel

connection = connect()
channel = open_channel(connection)

channel.basic_publish(exchange="", routing_key="test", body="Hello World!")

print("Sent 'Hello World!'")
connection.close()
