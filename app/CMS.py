from celery import Celery
import urllib.request
import os

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
