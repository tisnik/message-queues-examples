#!/usr/bin/env python

import base64

import stomp

destination = "/queue/test"

conn = stomp.Connection(host_and_ports=[("localhost", 61613)])
conn.start()
conn.connect(login="admin", passcode="admin")


with open("vim_editor.gif", mode="rb") as file:
    binaryData = file.read()
    print("Read {length} bytes from binary file".format(length=len(binaryData)))

    textData = base64.b64encode(binaryData)
    conn.send(destination, textData, persistent="true")
    print("Sent {length} characters".format(length=len(textData)))


conn.disconnect()
