"""Vytvoření úlohy."""

from slow_adder import add

r = add(1, 2)
print(r)
print(r())
print(r(blocking=True))
