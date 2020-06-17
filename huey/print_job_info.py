"""Vytvoření úlohy a vypsání podrobnějších informací o úloze."""

from adder import add

r = add(1, 2)
print("result id:\t", r.id)
print("task object:\t", r.task)
print("arguments:\t", r.task.args)
print("planned ETA:\t", r.task.eta)
print("retries:\t", r.task.retries)
print("priority:\t", r.task.priority)
