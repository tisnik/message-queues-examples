#!/usr/bin/env python
# vim: set fileencoding=utf-8

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

import time

import dramatiq
from dramatiq.brokers.redis import RedisBroker


def setup_broker():
    redis_broker = RedisBroker(host="localhost", port=6379)
    dramatiq.set_broker(redis_broker)
    return redis_broker


setup_broker()


def worker(name, parameter):
    print(
        "Worker {w}: working, received parameter: {param}".format(
            w=name, param=parameter
        )
    )
    time.sleep(1)
    print("Worker {w}: done".format(w=name))


@dramatiq.actor
def test_worker_A(parameter):
    worker("A", parameter)


@dramatiq.actor
def test_worker_B(parameter):
    worker("B", parameter)


@dramatiq.actor
def test_worker_C(parameter):
    worker("C", parameter)
