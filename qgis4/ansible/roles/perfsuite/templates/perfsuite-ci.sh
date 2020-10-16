#! /bin/bash
GRAFFITI=/tmp/graffiti
DATE=$(date +"%Y_%m_%d_%H_%M")

MAIL_ADDRESSES="{{ mail_addresses|join(' ') }}"
MAIL_SUBJECT=""
MAIL_BODY=""

sendmail(){
  for mail_address in $MAIL_ADDRESSES; do
      echo "$MAIL_BODY" | mail -s "$MAIL_SUBJECT" $mail_address
  done
}

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
MAIL_SUBJECT="[qgis4] QGIS Server PerfSuite failed"

rm -rf $GRAFFITI
cd QGIS-Server-PerfSuite/scenarios && sh run.sh && cd -
if [ -d $GRAFFITI ]
then
  scp -r $GRAFFITI qgis-test:/var/www/qgisdata/QGIS-tests/perf_test/graffiti/$DATE
else
  MAIL_BODY="No such directory '$GRAFFITI'."
  sendmail
fi

echo "Regressions analysis"
echo "--------------------"
if [ -d $GRAFFITI ]
then
  cd QGIS-Server-PerfSuite/scenarios && . graffiti/venv/bin/activate && python regressions.py
  if [ $? -eq 1 ]
  then
    MAIL_BODY="Regressions have been detected."
    sendmail
  fi
fi
