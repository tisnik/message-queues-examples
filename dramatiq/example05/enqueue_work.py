#!/usr/bin/env python
# vim: set fileencoding=utf-8

import time

from test_worker_5 import setup_broker, test_worker

import dramatiq
from dramatiq.brokers.redis import RedisBroker

setup_broker()

test_worker.send(42)
