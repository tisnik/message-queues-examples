#!/usr/bin/env python
# vim: set fileencoding=utf-8

from sys import argv, exit

from rabbitmq_connect import connect, open_channel


def run_producer(queue_name):
    connection = connect()
    channel = open_channel(connection)

    for i in range(1, 11):
        channel.basic_publish(
            exchange="", routing_key=queue_name, body="Hello World! #{i}".format(i=i)
        )

    print("Sent 'Hello World!' ten times into the queue \"{q}\"".format(q=queue_name))
    connection.close()


if len(argv) <= 1:
    print("Please provide queue name on the CLI")
    exit(1)

run_producer(argv[1])
