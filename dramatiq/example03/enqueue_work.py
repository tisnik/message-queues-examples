#!/usr/bin/env python
# vim: set fileencoding=utf-8

import time
import dramatiq

from dramatiq.brokers.redis import RedisBroker

from test_worker_3 import test_worker, setup_broker


setup_broker()

for i in range(1, 11):
    test_worker.send(i)
