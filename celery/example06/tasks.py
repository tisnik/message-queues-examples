# vim: set fileencoding=utf-8

from time import sleep
from celery import Celery

app = Celery("tasks")

app.config_from_object("celeryconfig")


@app.task
def add(x, y):
    print("Working, received parameters {} and {} to add".format(x, y))
    sleep(2)
    result = x + y
    print("Done with result {}".format(result))
    return result


@app.task
def multiply(x, y):
    print("Working, received parameters {} and {} to multiply".format(x, y))
    sleep(2)
    result = x * y
    print("Done with result {}".format(result))
    return result
