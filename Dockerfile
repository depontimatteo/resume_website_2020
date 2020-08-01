FROM python:3.7-slim

RUN apt-get update
RUN apt-get install dos2unix
RUN apt-get install -y nginx

COPY requirements.txt /
COPY conf/nginx.conf /etc/nginx
RUN pip3 install -r /requirements.txt

COPY . /flask
WORKDIR /flask

RUN dos2unix ./bin/docker_gunicorn_start.sh
RUN chmod +x ./bin/docker_gunicorn_start.sh

ENTRYPOINT ["./bin/docker_gunicorn_start.sh"]