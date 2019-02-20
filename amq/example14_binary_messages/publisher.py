#!/usr/bin/env python

import time
import stomp
import base64


destination = "/queue/test"

conn = stomp.Connection(host_and_ports=[("localhost", 61613)])
conn.start()
conn.connect(login="admin", passcode="admin")


with open("vim_editor.gif", mode="rb") as file:
    binaryData = file.read()
    print("Read {l} bytes from binary file".format(l=len(binaryData)))

    textData = base64.b64encode(binaryData)
    conn.send(destination, textData, persistent='true')
    print("Sent {l} characters".format(l=len(textData)))


conn.disconnect()
