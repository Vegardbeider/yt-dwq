import subprocess
import os

def download(url):
    print(subprocess.run(["pwd"]))
    print(subprocess.run(["ls"]))
    return subprocess.run(["download.sh", url])
