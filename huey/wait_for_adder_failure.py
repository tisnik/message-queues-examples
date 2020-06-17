"""Vytvoření úlohy."""

from adder import add

r = add(1, "foo")
print(r)
print(r())
print(r(blocking=True))
