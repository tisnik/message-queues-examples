#!/usr/bin/env python
# vim: set fileencoding=utf-8

import time
import dramatiq

from dramatiq.brokers.redis import RedisBroker

from test_worker_10 import test_worker_A, test_worker_B, test_worker_C, setup_broker_and_backend


setup_broker_and_backend()

for parameter in "XYZ":
    p = dramatiq.pipeline([
        test_worker_A.message(parameter),
        test_worker_B.message(),
        test_worker_C.message(),
        test_worker_A.message(),
        test_worker_B.message(),
        test_worker_C.message()
    ]).run()
    print(p.get_result(block=True, timeout=5000))
