# vim: set fileencoding=utf-8

from tasks import red_task, green_task, blue_task

red_task.apply_async(queue="red_queue")
green_task.apply_async(queue="green_queue")
blue_task.apply_async(queue="blue_queue")
