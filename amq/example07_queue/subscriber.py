#!/usr/bin/env python

import time
import stomp

from queue import Queue


class SimpleListener(object):

    def __init__(self, conn):
        self.conn = conn

    def on_message(self, headers, message):
        print("Received message: {m}, putting it into queue".format(m=message))
        self.queue.put(message)

    def on_error(self, headers, message):
        print("Received an error {e}".format(e=message))


q = Queue()

destination = "/queue/test"

conn = stomp.Connection([("localhost", 61613)])
conn.set_listener('', SimpleListener(q))
conn.start()

conn.connect(login="admin", passcode="admin")
conn.subscribe(id='simple_listener', destination=destination, ack='auto')

print("Waiting for messages...")

while True:
    item = q.get()
    if item == "exit":
        break

    print(item)
    q.task_done()

conn.disconnect()
