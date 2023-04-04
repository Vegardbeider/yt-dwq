import subprocess
import os

def download(url):
    print(subprocess.run(["pwd"]))
    print(subprocess.run(["ls -l"]))
    return subprocess.run(["bash download.sh", url])
