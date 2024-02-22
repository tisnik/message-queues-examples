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


app.conf.beat_schedule = {
    "run-every-two-seconds": {
        "task": "tasks.periodic_task",
        "schedule": 2,
        "args": (),
    },
}


@app.task
def periodic_task():
    print("Working, called @ {now}".format(now=datetime.now()))
    sleep(2)
    print("Done")
