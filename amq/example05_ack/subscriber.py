#!/usr/bin/env python

import time

import stomp


class SimpleListener:
    def __init__(self, conn):
        self.conn = conn

    def on_message(self, headers, message):
        print("Received message: {m}".format(m=message))
        print(headers)
        message_id = headers["message-id"]
        subscription = headers["subscription"]
        self.conn.ack(message_id, subscription)

    def on_error(self, headers, message):
        print("Received an error {e}".format(e=message))


destination = "/queue/test"

conn = stomp.Connection(host_and_ports=[("localhost", 61613)])
conn.set_listener("", SimpleListener(conn))
conn.start()

conn.connect(login="admin", passcode="admin")
conn.subscribe(id="simple_listener", destination=destination, ack="client")

print("Waiting for messages...")

while True:
    time.sleep(10)
