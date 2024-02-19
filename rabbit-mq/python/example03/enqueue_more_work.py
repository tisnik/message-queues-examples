#!/usr/bin/env python
# vim: set fileencoding=utf-8

from rabbitmq_connect import connect

connection, channel = connect()

for i in range(1, 11):
    channel.basic_publish(
        exchange="", routing_key="test", body="Hello World! #{i}".format(i=i)
    )

print("Sent 'Hello World!' ten times")
connection.close()
