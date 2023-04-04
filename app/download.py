import subprocess
import os

def download(url):
    return subprocess.run(["./download.sh", url])
