#!/usr/bin/env python
# vim: set fileencoding=utf-8


from test_worker_7 import setup_broker, test_worker_A, test_worker_B, test_worker_C

import dramatiq

setup_broker()

for i in range(1, 6):
    g = dramatiq.group([
        test_worker_A.message(i),
        test_worker_B.message(i),
        test_worker_C.message(i)
    ]).run()
