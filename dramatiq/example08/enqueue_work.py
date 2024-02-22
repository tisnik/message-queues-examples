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


from test_worker_8 import (
    setup_broker_and_backend,
    test_worker_A,
    test_worker_B,
    test_worker_C,
)

import dramatiq

setup_broker_and_backend()

for i in range(1, 6):
    print(i)
    g = dramatiq.group(
        [
            test_worker_A.message(str(i)),
            test_worker_B.message(str(i)),
            test_worker_C.message(str(i)),
        ]
    ).run()
    g.wait(timeout=20000)
