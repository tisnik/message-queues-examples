#!/usr/bin/env python
# vim: set fileencoding=utf-8


from test_worker_1 import setup_broker, test_worker

setup_broker()

test_worker.send()
