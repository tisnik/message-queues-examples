"""Úloha pro součet dvou hodnot."""

from huey import RedisHuey

huey = RedisHuey()


@huey.task()
def add(a, b):
    """Úloha pro součet dvou hodnot."""
    return a + b
