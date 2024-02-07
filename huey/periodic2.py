"""Periodicky se opakující úloha."""

from huey import RedisHuey, crontab

huey = RedisHuey()


@huey.periodic_task(crontab(minute='*/5'))
def periodic():
    print("*** NOW ***")
