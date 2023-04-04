import subprocess
from flask import Flask, render_template, request
from download import download

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        download(request.form["url"])
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run()