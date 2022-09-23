# vim: set fileencoding=utf-8

from time import sleep
from datetime import datetime
from celery import Celery
from celery.schedules import crontab

app = Celery("tasks")

app.config_from_object("celeryconfig")


app.conf.beat_schedule = {
    "run-every-two-seconds": {
        "task": "tasks.periodic_task",
        "schedule": 2,
        "args": (),
    },
}


@app.task
def periodic_task():
    print("Working, called @ {now}".format(now=datetime.now()))
    sleep(2)
    print("Done")
