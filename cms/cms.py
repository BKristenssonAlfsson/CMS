from celery import Celery
from cms.config import celeryconfig


app = Celery(include=['cms.tasks.tasks'])
app.config_from_object(celeryconfig)

if __name__ == '__main__':
        app.start()
