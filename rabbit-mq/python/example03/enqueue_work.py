#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
connection, channel = connect()

channel.basic_publish(exchange='',
                      routing_key='test',
                      body='Hello World!')

print("Sent 'Hello World!'")
connection.close()
