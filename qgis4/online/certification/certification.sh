#! /bin/bash

# download data
URL=http://cite.opengeospatial.org/teamengine/about/wms/1.3.0/site/

if [ ! -f data/shapefile/Autos.shp ]
then
  cd data
  wget $URL/data-wms-1.3.0.zip
  unzip data-wms-1.3.0.zip
  rm data-wms-1.3.0.zip
  cd -
fi

# build 3.4 branch
cd ../../QGIS-Server-CertifSuite/docker/3.4 && sh build.sh && cd -

# stop and restart
docker-compose down
docker-compose rm -f
docker-compose up -d
