#! /bin/bash

# download data
if [ ! -d "./data" ]
then
  mkdir data
  cd data && git clone https://github.com/qgis/QGIS-Training-Data && cd -
fi

# stop and restart
docker-compose down
docker-compose rm -f
docker network prune -f
docker-compose up -d
