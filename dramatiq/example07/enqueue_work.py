import time
import dramatiq

from dramatiq.brokers.redis import RedisBroker

from test_worker_7 import test_worker_A, test_worker_B, test_worker_C, setup_broker


setup_broker()

for i in range(1, 6):
    g = dramatiq.group([
        test_worker_A.message(i),
        test_worker_B.message(i),
        test_worker_C.message(i)
    ]).run()
