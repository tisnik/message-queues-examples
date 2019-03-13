# vim: set fileencoding=utf-8

# ---------------------------------------------------------------------
#
# Demonstrační příklady využívající knihovnu Celery.
#
# Příklad číslo 2: jednoduchý plánovač deseti úloh.
#
# ---------------------------------------------------------------------

from tasks import add

for i in range(10):
    add.delay(i, i)
