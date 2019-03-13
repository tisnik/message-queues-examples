# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Celery.
#
# Příklad číslo 2: jednoduchý plánovač úlohy.
#
# ---------------------------------------------------------------------

from tasks import add

result = add.delay(1, 2)
print(result)
print(result.backend)
print(result.ready())
print(result.get())
print(result.ready())

print(result.get(timeout=5))

result.forget()
