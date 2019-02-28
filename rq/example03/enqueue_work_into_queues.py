# vim: set fileencoding=utf-8

# This script is used and described in the following article:
# https://www.root.cz/clanky/pouziti-nastroje-rq-redis-queue-pro-spravu-uloh-zpracovavanych-na-pozadi/

from redis import Redis
from rq import Queue

from worker import do_work


q_low = Queue("low", connection=Redis())
q_high = Queue("high", connection=Redis())


for i in range(10):
    result = q_low.enqueue(do_work, i)
    result = q_high.enqueue(do_work, i)
    print(result)
