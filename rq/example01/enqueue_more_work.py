# vim: set fileencoding=utf-8

# This script is used and described in the following article:
# https://www.root.cz/clanky/pouziti-nastroje-rq-redis-queue-pro-spravu-uloh-zpracovavanych-na-pozadi/

from redis import Redis
from worker import do_work

from rq import Queue

q = Queue(connection=Redis())

for i in range(10):
    result = q.enqueue(do_work)
    print(result)
