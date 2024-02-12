#!/usr/bin/env python

from time import sleep

from rabbitmq_connect import connect, open_channel


def on_receive(ch, method, properties, body):
    print("Received %r" % body)
    sleep(1)
    print("Done processing %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def run_consumer(queue_name):
    connection = connect()
    channel = open_channel(connection, queue_name)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_receive,
                          queue=queue_name,
                          no_ack=False)
    print('Waiting for messages in queue "{q}". To exit press CTRL+C'.format(q=queue_name))
    print("...")
    channel.start_consuming()


run_consumer('test')
