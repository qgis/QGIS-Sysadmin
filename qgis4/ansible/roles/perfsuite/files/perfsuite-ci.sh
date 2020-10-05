#! /bin/bash
GRAFFITI=/tmp/graffiti
DATE=$(date +"%Y_%m_%d_%H_%M")

echo "Remove docker images"
echo "--------------------"
docker rmi qgisserver-perfsuite/2.18
docker rmi qgisserver-perfsuite/3.10
docker rmi qgisserver-perfsuite/3.14
docker rmi qgisserver-perfsuite/master

echo "Build new docker images"
echo "-----------------------"
cd QGIS-Server-PerfSuite/docker/2.18 && sh build.sh && cd -
cd QGIS-Server-PerfSuite/docker/3.10 && sh build.sh && cd -
cd QGIS-Server-PerfSuite/docker/3.14 && sh build.sh && cd -
cd QGIS-Server-PerfSuite/docker/master && sh build.sh && cd -

echo "Run graffiti"
echo "------------"
rm -rf $GRAFFITI
cd QGIS-Server-PerfSuite/scenarios && sh run.sh && cd -
if [ -d $GRAFFITI ]
then
  scp -r $GRAFFITI qgis-test:/var/www/qgisdata/QGIS-tests/perf_test/graffiti/$DATE
fi
