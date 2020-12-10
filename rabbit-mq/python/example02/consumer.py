#!/usr/bin/env python
# vim: set fileencoding=utf-8

from rabbitmq_connect import connect

connection, channel = connect()


def on_receive(ch, method, properties, body):
    print("Received %r" % body)


channel.basic_consume(on_receive,
                      queue='test',
                      no_ack=True)

print('Waiting for messages. To exit press CTRL+C')
print("...")
channel.start_consuming()
