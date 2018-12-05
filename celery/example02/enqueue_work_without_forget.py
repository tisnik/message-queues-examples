from tasks import add

for i in range(10):
    add.delay(i, i)
