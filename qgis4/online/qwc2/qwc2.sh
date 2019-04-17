#! /bin/bash
NAME=qwc2-demo-apps-build

# build new prod tarbal
rm -rf qwc2_demo
docker build -t $NAME .
id=$(docker create $NAME)
docker cp $id:/root/qwc2-demo-app/prod qwc2_demo
docker rm -v $id

docker rmi $NAME

# download data
if [ ! -d "$ROOT/data" ]
then
  sh download.sh
fi

# stop and restart
docker-compose down
docker-compose rm -f
docker network prune -f
docker-compose up -d
