FROM python:slim

MAINTAINER Anas Juwaidi <anas.didi95@gmail.com>

# Install python packages
COPY requirements.pip requirements.pip
RUN echo "Install python packages" \
    && pip install -r requirements.pip

# Create home directory
ARG DOCKER_USER_NAME
ARG DOCKER_USER_ID
ARG DOCKER_GROUP_ID
ENV DOCKER_USER_NAME ${DOCKER_USER_NAME:-root}
ENV DOCKER_USER_ID ${DOCKER_USER_ID:-0}
ENV DOCKER_GROUP_ID ${DOCKER_GROUP_ID:-0}
RUN echo "Create home directory for ${DOCKER_USER_NAME} with UID ${DOCKER_USER_ID}, GID ${DOCKER_GROUP_ID}" \
    ## Create directory
    && mkdir -p /home/code \
    ## Set permission
    && chown -R ${DOCKER_USER_ID}:${DOCKER_GROUP_ID} /home/code
WORKDIR /home/code
