from time import sleep
from celery import Celery

app = Celery('tasks')

app.config_from_object('celeryconfig')


@app.task
def add(x, y):
    print("Working, received parameters {} and {}".format(x, y))
    sleep(2)
    print("Done")
    return x + y
