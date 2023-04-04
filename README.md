# YT-DWQ
## YouTube Downloader with Queue

This small project uses the [yt-dlp](https://github.com/yt-dlp/yt-dlp#installation) project on github as the tool to download youtube videos. Furter using [Flask](https://flask.palletsprojects.com/en/2.2.x/), I have created a simple web interface to add videos to a queue and download them. The queue is stored in a [sqlite](https://sqlite.org/index.html) database. One by one the videos are downloaded and stored in the configuered folder. 

*NOTE: The queue is not yet implemented*

### Installation
Start by pulling the docker image from docker hub:
```bash
docker pull vegardbeider/yt-dwq
```
Then run the container:
```bash
docker run -d -p <hostport>:8000 --volume <hostpath>:/output vegardbeider/yt-dwq
```

### Reuse / distribution
You are free to use this project as you like. If you want to reuse parts of the code, please give credit to the original author. There are no guarantees that this project will work for you. Also, I am not responsible for any damage caused by this project. 