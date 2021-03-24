#!/bin/bash

IMAGE=${IMAGE:-kalemena/zeroconf}
VERSION=${VERSION:-latest}

# PREPARE
docker -v
docker pull python:3
docker pull ${IMAGE}:${VERSION} || true

# BUILD
docker build --pull --cache-from ${IMAGE}:${VERSION} \
    -t ${IMAGE}:${VERSION} \
    -f Dockerfile \
    --build-arg BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
    --build-arg VCS_REF=`git rev-parse --short HEAD` \
    --build-arg VERSION=${VERSION} .

# CHECK
docker ps -a
docker tag ${IMAGE}:${VERSION} ${IMAGE}:latest
docker images
