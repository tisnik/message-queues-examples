"""Úloha pro součet dvou hodnot."""

from huey import RedisHuey

from time import sleep

huey = RedisHuey()


@huey.task()
def add(a, b):
    """Úloha pro součet dvou hodnot."""
    sleep(5)
    return a + b
