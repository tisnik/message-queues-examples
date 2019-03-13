# vim: set fileencoding=utf-8

from tasks import periodic_task

for _ in range(10):
    periodic_task.delay()
