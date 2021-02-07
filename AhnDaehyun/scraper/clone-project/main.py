"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

import requests
from flask import Flask, render_template, request, redirect, send_file
from so_scrapper import get_db as so_get_db
from ww_scrapper import get_db as ww_get_db
from ro_scrapper import get_db as ro_get_db
from exporter import save_to_file

""

stackover = "https://stackoverflow.com/jobs?r=true&q="
wework = "https://weworkremotely.com/remote-jobs/search?term="
remoteok = "https://remoteok.io/remote-dev+"

app = Flask("Scrapper")
db = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/find")
def find():
    keyword = request.args.get("search")
    if keyword is None:
        return redirect("/")

    elif keyword not in db:
        keyword = keyword.lower()
        so_db = so_get_db(stackover+keyword)
        ww_db = ww_get_db(wework+keyword)
        ro_db = ro_get_db(f"https://remoteok.io/remote-dev+{keyword}-jobs")
        db[keyword] = so_db + ww_db + ro_db

    return render_template("find.html", db=db[keyword], search=keyword, count=len(db[keyword]))


@app.route("/export")
def export():
    try:
        keyword = request.args.get("search")
        if not keyword:
            raise Exception()
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0")
