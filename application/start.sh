#!/bin/bash

docker build -t todo-list .

WORKING_DIR=$(pwd) 
docker run -v "$WORKING_DIR:/root" -p 8081:8080 todo-list:latest
