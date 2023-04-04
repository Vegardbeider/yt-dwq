import subprocess
from flask import Flask, render_template, request
from download import download

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        result  = download(request.form["url"])
        if result.returncode == 0:
            print("Download successful")
            return render_template("index.html", result="Download successful")
        else:
            print("Download failed")
            return render_template("index.html", result="Download failed with code: "+str(result.returncode))
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run()