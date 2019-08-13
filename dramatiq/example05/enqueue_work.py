#!/usr/bin/env python
# vim: set fileencoding=utf-8

import time
import dramatiq

from dramatiq.brokers.redis import RedisBroker

from test_worker_5 import test_worker, setup_broker


setup_broker()

test_worker.send(42)
