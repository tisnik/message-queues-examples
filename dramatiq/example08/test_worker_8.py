#!/usr/bin/env python
# vim: set fileencoding=utf-8


import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend


def setup_broker_and_backend():
    redis_broker = RedisBroker(host="localhost", port=6379)
    result_backend = RedisBackend()
    dramatiq.set_broker(redis_broker)
    redis_broker.add_middleware(Results(backend=result_backend))
    return redis_broker


setup_broker_and_backend()


def worker(name, parameter):
    print(
        "Worker {w}: working, received parameter: {param}".format(
            w=name, param=parameter
        )
    )
    print("Worker {w}: done".format(w=name))


@dramatiq.actor(store_results=True)
def test_worker_A(parameter):
    worker("A", parameter)
    return parameter + "A"


@dramatiq.actor(store_results=True)
def test_worker_B(parameter):
    worker("B", parameter)
    return parameter + "B"


@dramatiq.actor(store_results=True)
def test_worker_C(parameter):
    worker("C", parameter)
    return parameter + "C"
