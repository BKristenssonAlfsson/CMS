
BROKER_URL = CELERY_RESULT_BACKEND = "amqp://guest@localhost//"
CELERY_ROUTES = {'test': {'queue': 'queue_test'}}
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
