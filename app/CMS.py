from celery import Celery
import urllib.request
import os

"""
The whole point of Celery is to run it as a separate process 
so that your webapp could off-load computationally intense 
tasks to it, so why are you trying to run Celery worker in the 
same process as your webapp? 
"""


BASEDIR="/Users/bk930576/Python/downloads"

app = Celery("CMS",
             backend="rpc://",
             broker="pyamqp://guest@localhost//")


@app.task
def download(url, filename):
    response = urllib.request.urlopen(url)
    data = response.read()
    with open(BASEDIR+"/"+filename,"wb") as file:
        file.write(data)
    file.close


@app.task
def list_all_files():
    return os.listdir(BASEDIR)
