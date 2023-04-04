FROM python:alpine3.17

RUN apk add yt-dlp
RUN pip install flask
COPY app.py app.py

RUN yt-dlp --version

CMD python3 -m flask run