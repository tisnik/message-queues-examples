from redis import Redis
from rq import Queue
from time import sleep

from worker import do_work


q_low = Queue("low", connection=Redis())
q_high = Queue("high", connection=Redis())

jobs = []

for i in range(11):
    job = q_low.enqueue(do_work, i)
    jobs.append(job)
    job = q_high.enqueue(do_work, i)
    jobs.append(job)

print("Zzz")

sleep(7)

print("Reading job results")

for job in jobs:
    print(job)
    result = job.result
    if result is not None:
        print(result)
