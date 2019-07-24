import time
import dramatiq

from dramatiq.brokers.redis import RedisBroker

from test_worker_1 import test_worker, setup_broker


setup_broker()

test_worker.send()
