# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Celery.
#
# Příklad číslo 1: jednoduchý plánovač úlohy.
#
# ---------------------------------------------------------------------

from tasks import add

result = add.delay(1, 2)
print(result)
print(result.backend)
