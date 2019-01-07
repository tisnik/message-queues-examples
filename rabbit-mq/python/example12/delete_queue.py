#!/usr/bin/env python
from sys import argv, exit
from rabbitmq_connect import connect


def delete_queue(queue_name):
    connection = connect()
    channel = connection.channel()
    channel.queue_delete(queue=queue_name)
    connection.close()


if len(argv) <= 1:
    print('Please provide queue name on the CLI')
    exit(1)

delete_queue(argv[1])
