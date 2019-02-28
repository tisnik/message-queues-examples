# vim: set fileencoding=utf-8

# This script is used and described in the following article:
# https://www.root.cz/clanky/pouziti-nastroje-rq-redis-queue-pro-spravu-uloh-zpracovavanych-na-pozadi/

from redis import Redis
from rq import Queue
from time import sleep

from worker import do_work


q_low = Queue("low", connection=Redis())
q_high = Queue("high", connection=Redis())

jobs = []

for i in range(10):
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
