#!/usr/bin/env python

import time
import stomp


destination1 = "/topic/event"
destination2 = "/topic/event2"

MESSAGES = 10

conn = stomp.Connection([("localhost", 61613)])
conn.start()
conn.connect(login="admin", passcode="admin")


transaction=conn.begin()
print(transaction)

for i in range(0, MESSAGES):
    message = "Hello world #{i}!".format(i=i)
    print("Publishing message: " + message)
    conn.send(destination1, message, persistent='true', transaction=transaction)
    conn.send(destination2, message, persistent='true', transaction=transaction)
    time.sleep(1)
    print("Done")

conn.commit(transaction=transaction)


conn.disconnect()
