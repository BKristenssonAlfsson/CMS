from cms.cms import app
import os

BASEDIR = "/Users/bk930576/Python/downloads/"


@app.task()
def enrollment(**kwargs):
    d = kwargs.get("name"), kwargs.get("timestamp")
    filename = 'enrollment.txt'

    complete_name = os.path.join(BASEDIR, filename)

    f = open(complete_name, "a+")
    f.write(str(d)+"\n")
    return None
