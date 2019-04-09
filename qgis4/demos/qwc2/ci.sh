#! /bin/bash
NAME=qwc2-demo-apps-build

# build new prod tarbal
docker build -t $NAME .
id=$(docker create $NAME)
docker cp $id:/root/qwc2-demo-apps/prod.tar.gz prod.tar.gz
docker rm -v $id

# deploy the tarball (static site)
# todo
