#!/usr/bin/env python
# vim: set fileencoding=utf-8

import time

from test_worker_8 import setup_broker_and_backend, test_worker_A, test_worker_B, test_worker_C

import dramatiq
from dramatiq.brokers.redis import RedisBroker

setup_broker_and_backend()

for i in range(1, 6):
    print(i)
    g = dramatiq.group([
        test_worker_A.message(str(i)),
        test_worker_B.message(str(i)),
        test_worker_C.message(str(i))
    ]).run()
    g.wait(timeout=20000)
