"""Úloha pro součet dvou hodnot."""

from time import sleep

from huey import RedisHuey

huey = RedisHuey()


@huey.task()
def add(a, b):
    """Úloha pro součet dvou hodnot."""
    sleep(5)
    return a + b
