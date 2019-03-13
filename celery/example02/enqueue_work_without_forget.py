# vim: set fileencoding=utf-8

from tasks import add

for i in range(10):
    add.delay(i, i)
