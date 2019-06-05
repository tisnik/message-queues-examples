# vim: set fileencoding=utf-8

import pika


def connect(where='localhost'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(where))
    return connection


def open_channel(connection, queue_name='test'):
    # pokus o nove vytvoreni fronty ve skutecnosti neovlivni jiz existujici frontu
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    return channel


def use_fanout(channel, exchange_name='fanout_exchange'):
    channel.exchange_declare(exchange=exchange_name,
                             exchange_type='fanout')


def bind_queue(channel, queue_name, exchange_name='fanout_exchange'):
    channel.queue_declare(queue=queue_name)
    channel.queue_bind(exchange=exchange_name,
                       queue=queue_name)
