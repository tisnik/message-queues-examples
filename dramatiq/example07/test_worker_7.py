import time

import dramatiq
from dramatiq.brokers.redis import RedisBroker


def setup_broker():
    redis_broker = RedisBroker(host="localhost", port=6379)
    dramatiq.set_broker(redis_broker)
    return redis_broker


setup_broker()


def worker(name, parameter):
    print("Worker {w}: working, received parameter: {param}".format(w=name, param=parameter))
    time.sleep(1)
    print("Worker {w}: done".format(w=name))


@dramatiq.actor
def test_worker_A(parameter):
    worker("A", parameter)


@dramatiq.actor
def test_worker_B(parameter):
    worker("B", parameter)


@dramatiq.actor
def test_worker_C(parameter):
    worker("C", parameter)
