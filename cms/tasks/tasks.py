from cms.cms import app
import os

"""Home base dir"""
#BASEDIR = "C:/Users/Björn/Python/downloads/"
"""Work base dir"""
BASEDIR = "/Users/bk930576/Python/downloads/"


@app.task()
def enrollment(**kwargs):
    print(kwargs)
    d = kwargs.get("name"), kwargs.get("timestamp"), kwargs.get("role")
    filename = 'enrollment.txt'

    complete_name = os.path.join(BASEDIR, filename)

    f = open(complete_name, "a+")
    f.write(str(d)+"\n")
    return None
