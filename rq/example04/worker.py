from time import sleep


def do_work(param):
    print("Working, received parameter {}".format(param))
    sleep(2)
    print("Done")
    return 1.0 / (param + 1.0)
