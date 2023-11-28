FROM python:3.10-alpine
RUN apk add --update pkgconfig
RUN apk add gcc
RUN apk add mariadb-dev build-base
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
