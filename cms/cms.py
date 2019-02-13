from celery import Celery
from cms.config import celeryconfig


"""
The whole point of Celery is to run it as a separate process 
so that your webapp could off-load computationally intense 
tasks to it, so why are you trying to run Celery worker in the 
same process as your webapp? 

https://www.linode.com/docs/development/python/task-queue-celery-rabbitmq/
"""


app = Celery("cms",
             backend="rpc://",
             broker="pyamqp://guest@localhost//",
             include=['cms.tasks'],
             )

"""
app = Celery()
app.config_from_object('celeryconfig')
"""

