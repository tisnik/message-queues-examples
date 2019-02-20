# vim: set fileencoding=utf-8

from redis import Redis
from rq import Queue
from time import sleep

from worker import do_work


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
