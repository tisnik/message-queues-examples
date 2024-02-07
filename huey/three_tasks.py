"""Několik různých úloh."""

from time import sleep

from huey import RedisHuey

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
