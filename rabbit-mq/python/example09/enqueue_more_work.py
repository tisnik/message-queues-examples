#!/usr/bin/env python
# vim: set fileencoding=utf-8

from sys import exit, argv
from rabbitmq_connect import connect, open_channel, use_fanout, bind_queue


def run_producer():
    connection = connect()
    channel = open_channel(connection)

    use_fanout(channel)
    bind_queue(channel, 'fronta1')
    bind_queue(channel, 'fronta2')
    bind_queue(channel, 'fronta3')

    for i in range(1, 11):
        channel.basic_publish(exchange='fanout_exchange',
                              routing_key='',
                              body='Hello World! #{i}'.format(i=i))

    print('Sent \'Hello World!\' ten times into three queues "fronta1", "fronta2", and "fronta3"')
    connection.close()


run_producer()
