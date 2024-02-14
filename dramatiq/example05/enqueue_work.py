#!/usr/bin/env python
# vim: set fileencoding=utf-8


from test_worker_5 import setup_broker, test_worker

setup_broker()

test_worker.send(42)
