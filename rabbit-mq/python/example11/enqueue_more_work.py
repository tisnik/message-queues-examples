#!/usr/bin/env python
# vim: set fileencoding=utf-8


from pika.spec import BasicProperties
from rabbitmq_connect import connect, open_channel


def run_producer():
    connection = connect()
    channel = open_channel(connection, queue_name='priority_queue_2', max_priority=10)

    for i in range(1, 11):
        priority = 5 * (i % 3)
        prop = BasicProperties(priority=priority)
        body = 'Hello World! #{i} msg with priority {p}'.format(i=i, p=priority)
        channel.basic_publish(exchange='',
                              routing_key='priority_queue_2',
                              body=body,
                              properties=prop)

    connection.close()


run_producer()
