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
