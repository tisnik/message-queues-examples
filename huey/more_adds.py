"""Vytvoření deseti úloh."""

from slow_adder import add

rs = []

print("Queueing...")

for i in range(1, 11):
    r = add(i, i)
    rs.append(r)

print("Done, waiting for results...")

for r in rs:
    print(r(blocking=True))
