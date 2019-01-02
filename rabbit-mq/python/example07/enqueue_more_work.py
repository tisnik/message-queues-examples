#!/usr/bin/env python
from rabbitmq_connect import connect, open_channel

connection = connect()
channel = open_channel(connection)


def run_producer(queue_name):
    for i in range(1, 11):
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='Hello World! #{i}'.format(i=i))

    print('Sent \'Hello World!\' ten times into the queue "{q}"'.format(q=queue_name))
    connection.close()


run_producer('test')
