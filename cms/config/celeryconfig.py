
BROKER_URL = CELERY_RESULT_BACKEND = "amqp://guest@localhost//"
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Stockholm'
"""
Need to set Celery heartbeat to 0 to avoid errors. Known bug in celery 4+
https://github.com/celery/celery/issues/4817
"""
CELERY_BROKER_HEARTBEAT = 0
