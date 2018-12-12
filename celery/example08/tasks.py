from time import sleep
from datetime import datetime
from celery import Celery

app = Celery('tasks')

app.config_from_object('celeryconfig')


@app.task
def red_task():
    print("Red task called @ {now}".format(now=datetime.now()))
    sleep(2)
    print("Red task done")


@app.task
def green_task():
    print("Green task called @ {now}".format(now=datetime.now()))
    sleep(2)
    print("Green task done")


@app.task
def blue_task():
    print("Blue task called @ {now}".format(now=datetime.now()))
    sleep(2)
    print("Blue task done")
