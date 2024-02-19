#!/usr/bin/env python
# vim: set fileencoding=utf-8

from rabbitmq_connect import connect

connection, channel = connect()

channel.basic_publish(exchange="", routing_key="test", body="Hello World!")

print("Sent 'Hello World!'")
connection.close()
