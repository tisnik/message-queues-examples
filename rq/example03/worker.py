# vim: set fileencoding=utf-8

# This script is used and described in the following article:
# https://www.root.cz/clanky/pouziti-nastroje-rq-redis-queue-pro-spravu-uloh-zpracovavanych-na-pozadi/

from time import sleep


def do_work(param):
    print("Working, received parameter {}".format(param))
    sleep(2)
    print("Done")
