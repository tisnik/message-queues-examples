# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Celery.
#
# Příklad číslo 2: implementace workera.
#
# ---------------------------------------------------------------------

from celery import Celery

app = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y
