# vim: set fileencoding=utf-8

from time import sleep


def do_work():
    print("Working")
    sleep(2)
    assert False
    print("Done")
