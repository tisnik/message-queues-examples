# vim: set fileencoding=utf-8

from redis import Redis
from rq import Queue

from worker import do_work


q = Queue(connection=Redis())

result = q.enqueue(do_work)
print(result)
