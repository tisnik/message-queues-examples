#!/usr/bin/env python
from sys import exit, argv
from rabbitmq_connect import connect, open_channel
from pika.spec import BasicProperties


def run_producer():
    connection = connect()
    channel = open_channel(connection, queue_name='priority_queue_3', max_priority=100)

    for i in range(0, 100):
        priority = 100 - i
        prop = BasicProperties(priority=priority)
        channel.basic_publish(exchange='',
                              routing_key='priority_queue_2',
                              body='Hello World! #{i} msg with priority {p}'.format(i=i, p=priority),
                              properties=prop)

    connection.close()


run_producer()
