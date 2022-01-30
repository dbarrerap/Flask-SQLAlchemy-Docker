# Dockerizing a Flask application with a MySQL database

## Prerequisites

* Docker (Engine + Compose)

## Install

    git clone https://github.com/dbarrerap/Flask-SQLAlchemy-Docker.git
    docker build .
    docker-composer up -d

## Description

- _docker build ._ will build the image from source
- _docker-compose up -d_ will pull the dependencies from Docker Hub and start the services
- Open an HTTP client (I use ThunderClient, a Visual Studio Code extension, you can use Postman if you wish)

## More Information

Endpoints can be found in the image repository at [Docker Hub](https://hub.docker.com/repository/docker/dbarrerap/flask-docker)