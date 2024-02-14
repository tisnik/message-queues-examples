#!/usr/bin/env python
# vim: set fileencoding=utf-8


from test_worker_4 import setup_broker, test_worker

setup_broker()

for i in range(1, 11):
    test_worker.send(i)
