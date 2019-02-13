import urllib.request
import os
from cms.cms import app

BASEDIR = "/Users/bk930576/Python/downloads"


@app.task
def download(url, filename):
    response = urllib.request.urlopen(url)
    data = response.read()
    with open(BASEDIR+"/"+filename, "wb") as file:
        file.write(data)
    file.close


@app.task
def test(temp):
    return print("HEJ HEJ HEJ HEJ HEJ", temp)


@app.task
def list_all_files():
    return os.listdir(BASEDIR)
