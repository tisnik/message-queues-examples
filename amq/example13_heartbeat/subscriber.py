#!/usr/bin/env python

import time
import stomp


class SimpleListener:

    def __init__(self, conn):
        self.conn = conn

    def on_message(self, headers, message):
        print("Received message: {m}".format(m=message))

    def on_error(self, headers, message):
        print("Received an error {e}".format(e=message))

    def on_disconnected(self):
        print("Disconnected")

    def on_heartbeat(self):
        print("Heartbeat")

    def on_heartbeat_timeout(self):
        print("Heartbeat timeout")


destination = "/topic/event"

conn = stomp.Connection([("localhost", 61613)], heartbeats=(0,1000))
conn.set_listener('', SimpleListener(conn))
conn.start()

conn.connect(login="admin", passcode="admin")
conn.subscribe(id='simple_listener', destination=destination, ack='auto')

print("Waiting for messages...")

while True:
    time.sleep(10)

print("Done...")
