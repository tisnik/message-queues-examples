#!/usr/bin/env python
from sys import exit, argv
from rabbitmq_connect import connect, open_channel, use_topic_exchange, bind_queue


def run_producer():
    connection = connect()
    channel = open_channel(connection)

    use_topic_exchange(channel)
    bind_queue(channel, 'europe_queue',
               routing_pattern='europe.*', exchange_name='topic_exchange')
    bind_queue(channel, 'asia_queue',
               routing_pattern='asia.*', exchange_name='topic_exchange')
    bind_queue(channel, 'americas_queue',
               routing_pattern='americas.*', exchange_name='topic_exchange')

    keys = ("europe.cr", "europe.sr", "europe.pl",
            "asia.china",
            "americas.canada", "americas.chile")
    for key in keys:
        print(key)
        channel.basic_publish(exchange='topic_exchange',
                              routing_key=key,
                              body='Hello World! #{k}'.format(k=key))

    print('Sent \'Hello World!\' to all selected regions')
    connection.close()


run_producer()
