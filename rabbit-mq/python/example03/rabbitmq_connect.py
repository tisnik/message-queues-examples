# vim: set fileencoding=utf-8

import pika


def connect(where='localhost', queue_name='test'):
    connection = pika.BlockingConnection(pika.ConnectionParameters(where))
    channel = connection.channel()

    # pokus o nove vytvoreni fronty ve skutecnosti neovlivni jiz existujici frontu
    channel.queue_declare(queue=queue_name)
    return connection, channel
