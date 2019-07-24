import time

import dramatiq
from dramatiq.brokers.redis import RedisBroker


def setup_broker():
    redis_broker = RedisBroker(host="localhost", port=6379)
    dramatiq.set_broker(redis_broker)
    return redis_broker


setup_broker()


@dramatiq.actor
def test_worker():
    print("Working")
    time.sleep(1)
    print("Done")
