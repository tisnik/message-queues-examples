# vim: set fileencoding=utf-8

import pika


def connect(where='localhost'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(where))
    return connection


def open_channel(connection, queue_name='test', max_priority=10):
    # pokus o nove vytvoreni fronty ve skutecnosti neovlivni jiz existujici frontu
    channel = connection.channel()
    channel.queue_declare(queue=queue_name, arguments={"x-max-priority": max_priority})
    return channel
