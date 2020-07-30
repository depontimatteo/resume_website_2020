FROM python:3.7-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /flask
WORKDIR /flask

ENTRYPOINT ["./bin/docker_gunicorn_start.sh"]