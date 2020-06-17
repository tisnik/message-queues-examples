"""Několik různých úloh."""

from huey import RedisHuey

from time import sleep

huey = RedisHuey()

@huey.task()
def add(a, b):
    """Úloha pro rychlý součet dvou hodnot."""
    return a + b


@huey.task()
def slow_add(a, b):
    """Úloha pro pomalý součet dvou hodnot."""
    sleep(5)
    return a + b


@huey.task()
def mul(a, b):
    """Úloha pro součin dvou hodnot."""
    return a * b
