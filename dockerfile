FROM python:alpine3.17

RUN apk add --no-cache yt-dlp
#RUN python3 -m venv /.venv/flask
#RUN source /.venv/flask/bin/activate
RUN pip install flask gunicorn

COPY app /app

WORKDIR /app

CMD gunicorn -w 1 -b 0.0.0.0 webGUI:app