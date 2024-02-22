# Copyright © 2019 Pavel Tisnovsky
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
