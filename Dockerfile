# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /python-docker

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
