#! /bin/bash
NAME=qwc2-demo-apps-build

# build new prod tarbal
docker build -t $NAME .
id=$(docker create $NAME)
docker cp $id:/root/qwc2-demo-app/prod demos_qwc2
docker rm -v $id
