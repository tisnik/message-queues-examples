# vim: set fileencoding=utf-8

# This script is used and described in the following article:
# https://www.root.cz/clanky/pouziti-nastroje-rq-redis-queue-pro-spravu-uloh-zpracovavanych-na-pozadi/

from time import sleep

from redis import Redis
from worker import do_work

from rq import Queue

q_failed = Queue("failed", connection=Redis())

print("Reading failed jobs")

job_ids = q_failed.job_ids

print(job_ids)

for job_id in job_ids:
    print(job_id)
    job = q_failed.fetch_job(job_id)
    print(job.origin)
    print(job.enqueued_at)
    print(job.started_at)
    print(job.ended_at)
    print(job.exc_info)
