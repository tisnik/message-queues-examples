from redis import Redis
from rq import Queue

from worker import do_work


q = Queue(connection=Redis())

result = q.enqueue(do_work, 0)
print(result)