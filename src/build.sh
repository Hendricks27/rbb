#!/bin/bash

tag="V0.1.1"

docker build --platform linux/amd64 -t wenjin27/rbb:$tag -t wenjin27/rbb:latest ./

docker push wenjin27/rbb:$tag
docker push wenjin27/rbb:latest

# docker run -p 10981:10981 wenjin27/rbb

