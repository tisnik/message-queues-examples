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

from datetime import datetime
from time import sleep

from celery import Celery

app = Celery("tasks")

app.config_from_object("celeryconfig")


@app.task
def red_task():
    print("Red task called @ {now}".format(now=datetime.now()))
    sleep(2)
    print("Red task done")


@app.task
def green_task():
    print("Green task called @ {now}".format(now=datetime.now()))
    sleep(2)
    print("Green task done")


@app.task
def blue_task():
    print("Blue task called @ {now}".format(now=datetime.now()))
    sleep(2)
    print("Blue task done")
