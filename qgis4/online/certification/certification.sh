#! /bin/bash

# download data
URL=http://cite.opengeospatial.org/teamengine/about/wms/1.3.0/site/

if [ ! -f data/shapefile/Autos.shp ]
then
  cd data
  wget $URL/data-wms-1.3.0.zip
  unzip data-wms-1.3.0.zip
  rm data-wms-1.3.0.zip
  git clone https://github.com/qgis/QGIS-Training-Data
  cd -
fi

# build 3.10 branch
cd ../../QGIS-Server-CertifSuite/docker/3.10 && sh build.sh && cd -

# stop and restart
docker-compose down
docker-compose rm -f
docker network prune -f
docker-compose up -d
