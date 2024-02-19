#!/usr/bin/env python
from rabbitmq_connect import connect, open_channel


def run_producer(queue_name):
    connection = connect()
    channel = open_channel(connection, queue_name)

    channel.basic_publish(exchange="", routing_key=queue_name, body="Hello World!")

    print("Sent 'Hello World!' message into the queue \"{q}\"".format(q=queue_name))

    connection.close()


run_producer("test")
