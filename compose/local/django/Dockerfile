FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./requirements /root/requirements
RUN set -xe \
        && apt-get update -y \
        && apt-get install -y \
            build-essential \
            curl \
            default-libmysqlclient-dev \
            libjpeg-dev \
            libpq-dev \
        && pip3 install -r /root/requirements/local.txt
