"""Vytvoření deseti úloh."""

from slow_adder import add

print("Queueing...")
rg = add.map([(i, i) for i in range(1, 11)])

print("Done, waiting for results...")

print(rg.get(blocking=True))
