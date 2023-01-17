#!/bin/bash

tag="V0.1.1"

docker build --platform linux/amd64 -t wenjin27/rbb:$tag -t wenjin27/rbb:latest ./

# docker push wenjin27/rbb:$tag
# docker push wenjin27/rbb:latest

docker tag wenjin27/rbb:latest 174329956306.dkr.ecr.us-east-1.amazonaws.com/rbb:latest
docker tag wenjin27/rbb:latest 174329956306.dkr.ecr.us-east-1.amazonaws.com/rbb:$tag

docker push 174329956306.dkr.ecr.us-east-1.amazonaws.com/rbb:latest
docker push 174329956306.dkr.ecr.us-east-1.amazonaws.com/rbb:$tag

# docker run -p 10981:10981 wenjin27/rbb

