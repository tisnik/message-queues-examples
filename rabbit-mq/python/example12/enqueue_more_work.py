#!/usr/bin/env python
# vim: set fileencoding=utf-8

from sys import exit, argv
from rabbitmq_connect import connect, open_channel
from pika.spec import BasicProperties


def run_producer():
    connection = connect()
    channel = open_channel(connection, queue_name='priority_queue_3', max_priority=100)

    for i in range(0, 100):
        priority = 100 - i
        prop = BasicProperties(priority=priority)
        body = 'Hello World! #{i} msg with priority {p}'.format(i=i, p=priority)
        channel.basic_publish(exchange='',
                              routing_key='priority_queue_3',
                              body=body,
                              properties=prop)

    connection.close()


run_producer()
