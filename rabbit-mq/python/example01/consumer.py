#!/usr/bin/env python
# vim: set fileencoding=utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# pokus o nove vytvoreni fronty ve skutecnosti neovlivni jiz existujici frontu
channel.queue_declare(queue='test')


def on_receive(ch, method, properties, body):
    print("Received %r" % body)


channel.basic_consume(on_receive,
                      queue='test',
                      no_ack=True)

print('Waiting for messages. To exit press CTRL+C')
print("...")
channel.start_consuming()
