#! /bin/sh
WMS130=/tmp/certifsuite-wms130
WFS110=/tmp/certifsuite-wfs110
DATE=$(date +"%Y_%m_%d_%H_%M")

echo "Remove docker images for master"
echo "------------------------------"
docker rmi qgisserver-certifsuite/master

echo "Build new docker image for master"
echo "---------------------------------"
cd QGIS-Server-CertifSuite/docker/master && sh build.sh && cd -

echo "Run OGC tests for WMS 1.3.0"
echo "---------------------------"
rm -rf $WMS130
cd QGIS-Server-CertifSuite/testsuite/wms-1.3.0/ && sh run.sh && cd -
if [ -d $WMS130 ]
then
  rm -f $WMS130/report.xml
  scp -r $WMS130 qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wms_130/$DATE
  scp -r $WMS130/* qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wms_130/latest/
fi

echo "Run OGC tests for WFS 1.1.0"
echo "---------------------------"
rm -rf $WFS110
cd QGIS-Server-CertifSuite/testsuite/wfs-1.1.0/ && sh run.sh && cd -
if [ -d $WFS110 ]
then
  scp -r $WFS110 qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wfs_110/$DATE
  scp -r $WFS110/* qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wfs_110/latest/
fi
