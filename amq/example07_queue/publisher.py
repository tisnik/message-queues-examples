#!/usr/bin/env python


import stomp

destination1 = "/queue/test"
destination2 = "/queue/test2"

MESSAGES = 10

conn = stomp.Connection([("localhost", 61613)])
conn.start()
conn.connect(login="admin", passcode="admin")


for i in range(0, MESSAGES):
    message = "Hello world #{i}!".format(i=i)
    conn.send(destination1, message, persistent='true')
    conn.send(destination2, message, persistent='true')


conn.send(destination1, "exit", persistent='true')
conn.send(destination2, "exit", persistent='true')

conn.disconnect()

print("Done")
