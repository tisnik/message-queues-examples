#!/usr/bin/env python

import time

import stomp

destination1 = "/topic/event"
destination2 = "/topic/event2"

MESSAGES = 10

conn = stomp.Connection([("localhost", 61613)], heartbeats=(0, 0))
conn.start()
conn.connect(login="admin", passcode="admin")


for i in range(0, MESSAGES):
    message = "Hello world #{i}!".format(i=i)
    print("Publishing message: " + message)
    conn.send(destination1, message, persistent='true')
    conn.send(destination2, message, persistent='true')
    time.sleep(0.5)
    print("Done")


conn.disconnect()
