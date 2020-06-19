"""Periodicky se opakující úloha."""

from huey import crontab
from huey import RedisHuey

huey = RedisHuey()

@huey.periodic_task(crontab(minute='*/5'))
def periodic():
    print("*** NOW ***")
