"""Vytvoření úlohy."""

from adder import add

r = add(1, "foo")
print(r)
print(r())

try:
    print(r(blocking=True))
except Exception as e:
    print("Exception detected!", e)
