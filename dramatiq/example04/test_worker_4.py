#!/usr/bin/env python
# vim: set fileencoding=utf-8

import time

import dramatiq
from dramatiq.brokers.redis import RedisBroker


def setup_broker():
    redis_broker = RedisBroker(host="localhost", port=6379)
    dramatiq.set_broker(redis_broker)
    return redis_broker


setup_broker()


@dramatiq.actor(max_retries=3)
def test_worker(parameter):
    print("Working, received parameter: {param}".format(param=parameter))
    if parameter % 3 == 0:
        raise Exception("I don't like this parameter!")
    time.sleep(1)
    print("Done")
