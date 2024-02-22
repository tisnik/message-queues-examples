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


import dramatiq
from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends import RedisBackend


def setup_broker_and_backend():
    redis_broker = RedisBroker(host="localhost", port=6379)
    result_backend = RedisBackend()
    dramatiq.set_broker(redis_broker)
    redis_broker.add_middleware(Results(backend=result_backend))
    return redis_broker


setup_broker_and_backend()


def worker(name, parameter):
    print(
        "Worker {w}: working, received parameter: {param}".format(
            w=name, param=parameter
        )
    )
    print("Worker {w}: done".format(w=name))


@dramatiq.actor(store_results=True)
def test_worker_A(parameter):
    worker("A", parameter)
    return parameter + "A"


@dramatiq.actor(store_results=True)
def test_worker_B(parameter):
    worker("B", parameter)
    return parameter + "B"


@dramatiq.actor(store_results=True)
def test_worker_C(parameter):
    worker("C", parameter)
    return parameter + "C"
