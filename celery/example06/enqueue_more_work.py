from tasks import add, multiply

for i in range(10):
    add.apply_async((i, i + 1), link=multiply.s(i))
