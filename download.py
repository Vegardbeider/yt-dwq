import subprocess
import os

def download(url):
    subprocess.run(["./download.sh", url])
