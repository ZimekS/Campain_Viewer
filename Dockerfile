# pull official base image
FROM python:3.10.7-slim-buster

# set work directory
WORKDIR /usr/src/campViewer

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/campViewer/requirements.txt
RUN pip install -r requirements.txt

# copy project
#COPY main.py .
COPY . /usr/src/campViewer

ENTRYPOINT ["/usr/src/campViewer/entrypoint.sh"]