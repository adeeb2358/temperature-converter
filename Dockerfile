# base image is python 3.9
FROM python:3.9
# dump log message immediately to the stream instead of being buffered
ENV PYTHONBUFFERED=1
# setting the work directory inside the docker
WORKDIR /app
#copy the requirments file to work directory
COPY requirements.txt /app/requirements.txt
#python package manager upgrade
RUN pip3 install --upgrade pip
# install unicorn stantard seperately. It doesnt have websocket support for basic installation
RUN pip3 install pip 'uvicorn[standard]'
# install necessary dependecies
RUN pip3 install -r /app/requirements.txt
#install test framework
RUN pip3 install -U pytest
RUN pip3 install -U pytest-cov

#copy everything in the source folder of host machine to docker
COPY . /app

EXPOSE 8000

