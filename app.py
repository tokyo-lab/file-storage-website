from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/your-url", methods=["GET", "POST"])
def your_url():
    if request.method == "POST":
        urls = {}

        if os.path.exists("urls.json"):
            with open("urls.json") as urls_file:
                urls = json.load(urls_file)
        if request.form["code"] in urls.keys():
            flash(
                "That shortname has already been taken. Please enter a different shortname"
            )
            return redirect(url_for("home"))

        urls[request.form["code"]] = {"url": request.form["url"]}
        with open("urls.json", "w") as url_file:
            json.dump(urls, url_file)
        return render_template("your_url.html", code=request.form["code"])
    else:
        return redirect(url_for("home"))
