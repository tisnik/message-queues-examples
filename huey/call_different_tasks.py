"""Vytvoření různých úloh."""

from three_tasks import add, mul, slow_add

rs = []

print("Queueing...")

for i in range(1, 11):
    rs.append(add(i, i))
    rs.append(slow_add(i, i))
    rs.append(mul(i, i))

print("Done, waiting for results...")

for r in rs:
    print(r(blocking=True))
