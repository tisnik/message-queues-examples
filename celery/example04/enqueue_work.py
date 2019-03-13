# vim: set fileencoding=utf-8

from tasks import add

async_tasks = []
for i in range(10):
    async_tasks.append(add.delay(i, i))

for task in async_tasks:
    print(task)
    print(task.backend)
    print(task.ready())
    print(task.get())
    print(task.ready())

    print(task.get(timeout=5))

    task.forget()
