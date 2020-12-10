#!/usr/bin/env python

from time import sleep
from rabbitmq_connect import connect, open_channel

connection = connect()
channel = open_channel(connection)


def on_receive(ch, method, properties, body):
    print("Received %r" % body)
    sleep(5)
    print("Done processing %r" % body)
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_receive,
                      queue='test',
                      no_ack=False)

print('Waiting for messages. To exit press CTRL+C')
print("...")
channel.start_consuming()
