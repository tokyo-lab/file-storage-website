from flask import Flask, render_template, request, redirect, url_for, flash, abort
import json
import os.path
from werkzeug.utils import secure_filename

from rich import print as printc
from rich.console import Console

console = Console()

app = Flask(__name__)
app.secret_key = "h432hi5ohi3h5i5hi3o2hi"


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
                "That short name has already been taken. Please enter a different one"
            )
            return redirect(url_for("home"))

        if "url" in request.form.keys():
            urls[request.form["code"]] = {"url": request.form["url"]}

        else:
            f = request.files["file"]
            full_name = secure_filename(str(f.filename))
            path = (
                "/Users/michaelmena/Documents/orange/url-shortener/static/user_files/"
                + full_name
            )

            printc("[green][+] This is f: [/green]", f)
            printc("[green][+] This is fullname: [/green]", full_name)
            f.save(path)
            urls[request.form["code"]] = {"file": full_name}

        with open("urls.json", "w") as url_file:
            json.dump(urls, url_file)
        return render_template("your_url.html", code=request.form["code"])
    else:
        return redirect(url_for("home"))


@app.route("/<string:code>")
def redirect_to_url(code):
    printc("[blue][+] This is code: [/blue]", code)
    if os.path.exists("urls.json"):
        with open("urls.json") as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if "url" in urls[code].keys():
                    return redirect(urls[code]["url"])
                else:
                    return redirect(
                        url_for("static", filename="user_files/" + urls[code]["file"])
                    )
    return abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404
