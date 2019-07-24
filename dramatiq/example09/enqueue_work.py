import time
import dramatiq

from dramatiq.brokers.redis import RedisBroker

from test_worker_9 import test_worker_A, test_worker_B, test_worker_C, setup_broker_and_backend


setup_broker_and_backend()

p = dramatiq.pipeline([
    test_worker_A.message("!"),
    test_worker_B.message(),
    test_worker_C.message()
]).run()

print(p.get_result(block=True, timeout=5000))
