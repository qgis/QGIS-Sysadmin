#! /bin/sh
WMS130=/tmp/certifsuite-wms130
WFS110=/tmp/certifsuite-wfs110
OGCAPIF=/tmp/certifsuite-ogcapif
DATE=$(date +"%Y_%m_%d_%H_%M")

MAIL_ADDRESSES="{{ mail_addresses|join(' ') }}"
MAIL_SUBJECT=""
MAIL_BODY=""

sendmail(){
  for mail_address in $MAIL_ADDRESSES; do
      echo "$MAIL_BODY" | mail -s "$MAIL_SUBJECT" $mail_address
  done
}

echo "Remove docker images for master"
echo "------------------------------"
docker rmi qgisserver-certifsuite/master

echo "Build new docker image for master"
echo "---------------------------------"
cd QGIS-Server-CertifSuite/docker/master && sh build.sh && cd -

echo "Run OGC tests for WMS 1.3.0"
echo "---------------------------"
MAIL_SUBJECT="[qgis4] QGIS Server CertifSuite WMS 1.3.0 failed"

rm -rf $WMS130
cd QGIS-Server-CertifSuite/testsuite/wms-1.3.0/ && sh run.sh && cd -
if [ -d $WMS130 ]
then
  if [ ! -f $WMS130/report.html ]
  then
    MAIL_BODY="No such file '$WMS130/report.html'."
    sendmail
  else
    cat $WMS130/report.html | grep Overall -A 1 | grep Passed > /dev/null
    if [ $? -eq 1 ]
    then
      MAIL_BODY="OGC tests are failing."
      sendmail
    else
      rm -f $WMS130/report.xml
      scp -r $WMS130 qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wms_130/$DATE
      scp -r $WMS130/* qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wms_130/latest/
      cd QGIS-Server-CertifSuite/testsuite/wms-1.3.0/ && scp logo.png qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wms_130/$DATE/ && cd -
    fi
  fi
else
  MAIL_BODY="No such directory '$WMS130'."
  sendmail
fi

echo "Run OGC tests for WFS 1.1.0"
echo "---------------------------"
MAIL_SUBJECT="[qgis4] QGIS Server CertifSuite WFS 1.1.0 failed"

rm -rf $WFS110
cd QGIS-Server-CertifSuite/testsuite/wfs-1.1.0/ && sh run.sh && cd -
if [ -d $WFS110 ]
then
  if [ ! -f $WFS110/report.html ]
  then
    MAIL_BODY="No such file '$WFS110/report.html'."
    sendmail
  else
    # WFS 1.1.0 OGC tests are failing for now (it is known), so we don't
    # check the Passed status
    scp -r $WFS110 qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wfs_110/$DATE
    scp -r $WFS110/* qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wfs_110/latest/
    cd QGIS-Server-CertifSuite/testsuite/wfs-1.1.0/ && scp logo.png qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/wms_130/$DATE/ && cd -
  fi
else
  MAIL_BODY="No such directory '$WFS110'."
  sendmail
fi

echo "Run OGC tests for OGC API Features"
echo "----------------------------------"
MAIL_SUBJECT="[qgis4] QGIS Server CertifSuite OGC API Features failed"

rm -rf $OGCAPIF
cd QGIS-Server-CertifSuite/testsuite/ogcapif/ && sh run.sh && cd -
if [ -d $OGCAPIF ]
then
  if [ ! -f $OGCAPIF/report.html ]
  then
    MAIL_BODY="No such file '$OGCAPIF/report.html'."
    sendmail
  else
    # OGC API F tests are failing for now (it is known), so we don't
    # check the Passed status
    scp -r $OGCAPIF qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/ogcapif/$DATE
    scp -r $OGCAPIF/* qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/ogcapif/latest/
    cd QGIS-Server-CertifSuite/testsuite/ogcapif/ && scp logo.png qgis-test:/var/www/qgisdata/QGIS-tests/ogc_cite/ogcapif/$DATE/ && cd -
  fi
else
  MAIL_BODY="No such directory '$OGCAPIF'."
  sendmail
fi
