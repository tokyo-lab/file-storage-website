from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", name="Cooper")


@app.route("/your-url")
def your_url():
    return render_template("your_url.html")
