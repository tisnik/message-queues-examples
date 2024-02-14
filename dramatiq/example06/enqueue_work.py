#!/usr/bin/env python
# vim: set fileencoding=utf-8


from test_worker_6 import setup_broker, test_worker_A, test_worker_B, test_worker_C

setup_broker()

for i in range(1, 6):
    test_worker_A.send(i)
    test_worker_B.send(i)
    test_worker_C.send(i)
