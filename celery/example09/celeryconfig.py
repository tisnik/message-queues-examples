broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'

task_send_sent_event = True

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True

task_default_queue = 'celery'

worker_log_color = True

task_routes = {
    'tasks.red_task':   {'queue': 'red_queue'},
    'tasks.green_task': {'queue': 'green_queue'},
    'tasks.blue_task':  {'queue': 'blue_queue'},
}